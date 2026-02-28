import numpy as np
import cv2
from scipy.ndimage import label
import os

def simulate_and_save(input_data: str, width: int = 101, height: int = 103, max_time: int = 100000, threshold: int = 40) -> None:
    robots = []
    for line in input_data.strip().split('\n'):
        p, v = line.split(' v=')
        px, py = map(int, p[2:].split(','))
        vx, vy = map(int, v.split(','))
        robots.append((px, py, vx, vy))

    for time in range(max_time):
        grid = np.zeros((height, width), dtype=int)

        for px, py, vx, vy in robots:
            new_x = (px + vx * time) % width
            new_y = (py + vy * time) % height
            grid[new_y, new_x] = 1

        labeled_grid, _ = label(grid)
        cluster_sizes = np.bincount(labeled_grid.ravel())[1:]

        if any(size >= threshold for size in cluster_sizes):
            print(f'Large cluster found at time {time}, saving image...')
            save_grid_as_image(grid, f'step_{time}.png')

def save_grid_as_image(grid: np.ndarray, filename: str) -> None:
    img = (grid * 255).astype(np.uint8)
    img_colored = cv2.applyColorMap(img, cv2.COLORMAP_JET)

    filename = os.path.join('outputs', filename)
    cv2.imwrite(filename, img_colored)
    print(f'Image saved in {os.path.abspath(filename)}')

input_data = open('../inputs/input14.txt', 'r').read()
simulate_and_save(input_data)