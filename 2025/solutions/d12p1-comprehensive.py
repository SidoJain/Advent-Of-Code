from typing import NamedTuple

Coord = tuple[int, int]
ShapeCoords = tuple[Coord, ...]

PLACEMENT_CACHE: dict[tuple[int, int, int], list[int]] = {}

class RegionSpec(NamedTuple):
    width: int
    height: int
    requirements: dict[int, int]

class ProblemInput(NamedTuple):
    shapes: dict[int, ShapeCoords]
    regions: list[RegionSpec]

def normalize_shape(coords: set[Coord]) -> ShapeCoords:
    if not coords: return ()
    min_r = min(row for row, _ in coords)
    min_c = min(col for _, col in coords)
    return tuple(sorted((row - min_r, col - min_c) for row, col in coords))

def parse_input(raw_input: str) -> ProblemInput:
    blocks = raw_input.strip().split('\n\n')
    shapes = {}
    regions = []

    for block in blocks:
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        if not lines:
            continue

        header = lines[0]
        if header.endswith(':') and 'x' not in header:
            shape_idx = int(header[:-1])
            coords = set()
            for row, line in enumerate(lines[1:]):
                for col, char in enumerate(line):
                    if char == '#': coords.add((row, col))
            shapes[shape_idx] = normalize_shape(coords)
        else:
            for line in lines:
                dims, counts = line.split(':')
                w, h = map(int, dims.split('x'))
                reqs = {i: col for i, col in enumerate(map(int, counts.split())) if col > 0}
                regions.append(RegionSpec(w, h, reqs))
    return ProblemInput(shapes, regions)

def coords_to_bitmask(coords: ShapeCoords, board_w: int) -> int:
    mask = 0
    for row, col in coords:
        mask |= (1 << (row * board_w + col))
    return mask

def get_placements(shape_id: int, shape: ShapeCoords, board_w: int, board_h: int) -> list[int]:
    cache_key = (shape_id, board_w, board_h)
    if cache_key in PLACEMENT_CACHE:
        return PLACEMENT_CACHE[cache_key]

    variations = set()
    current = shape
    for _ in range(4):
        variations.add(normalize_shape(set(current)))
        current = tuple((col, -row) for row, col in current)
    current = tuple((row, -col) for row, col in shape)
    for _ in range(4):
        variations.add(normalize_shape(set(current)))
        current = tuple((col, -row) for row, col in current)

    valid_masks = set()
    for var in variations:
        if not var:
            continue
        height = max(row for row, _ in var) + 1
        width = max(col for _, col in var) + 1

        base_mask = coords_to_bitmask(var, board_w)
        for row in range(board_h - height + 1):
            for col in range(board_w - width + 1):
                shift = (row * board_w) + col
                valid_masks.add(base_mask << shift)

    result = sorted(list(valid_masks)) 
    PLACEMENT_CACHE[cache_key] = result
    return result

def solve_region(region: RegionSpec, shapes_lib: dict[int, ShapeCoords]) -> bool:
    piece_ids = []
    for s_idx, count in region.requirements.items():
        piece_ids.extend([s_idx] * count)

    piece_areas = {pid: len(shapes_lib[pid]) for pid in set(piece_ids)}
    piece_ids.sort(key=lambda p: (piece_areas[p], p), reverse=True)

    total_area = sum(piece_areas[p] for p in piece_ids)
    if total_area > region.width * region.height:
        return False

    moves_cache = {}
    for pid in set(piece_ids):
        moves = get_placements(pid, shapes_lib[pid], region.width, region.height)
        if not moves: return False
        moves_cache[pid] = moves

    def backtrack(idx: int, board: int, last_move_index: int) -> bool:
        if idx == len(piece_ids):
            return True

        pid = piece_ids[idx]
        possible_moves = moves_cache[pid]
        start_i = 0
        if idx > 0 and piece_ids[idx] == piece_ids[idx-1]:
            start_i = last_move_index + 1

        for i in range(start_i, len(possible_moves)):
            move = possible_moves[i]
            if (board & move) == 0:
                if backtrack(idx + 1, board | move, i):
                    return True
        return False

    return backtrack(0, 0, -1)

with open("../inputs/input12.txt", "r") as file:
    raw_input = file.read()
problem = parse_input(raw_input)

fit_count = 0
for region in problem.regions:
    if solve_region(region, problem.shapes):
        fit_count += 1
print(fit_count)