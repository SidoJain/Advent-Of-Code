def parseInput(filename: str) -> tuple[list[int], list[int]]:
    with open(filename) as file:
        time, dist = file.readlines()
        time = [int(num) for num in time.strip().split()[1:]]
        dist = [int(num) for num in dist.strip().split()[1:]]
    return time, dist

def countWaysToWin(times: list[int], distances: list[int]) -> int:
    total_margin = 1
    for max_time, record_distance in zip(times, distances):
        ways_to_win = 0
        for hold_time in range(1, max_time):
            speed = hold_time
            travel_time = max_time - hold_time
            distance_traveled = speed * travel_time
            if distance_traveled > record_distance:
                ways_to_win += 1
        total_margin *= ways_to_win
    return total_margin

time, dist = parseInput('../inputs/input6.txt')
print(countWaysToWin(time, dist))