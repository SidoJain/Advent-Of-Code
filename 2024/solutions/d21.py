from enum import Enum
from functools import cache
from typing import NamedTuple, Iterator

class Position(NamedTuple):
    x: int
    y: int

class KeypadType(Enum):
    NUMPAD = 0
    DIRPAD = 1

    def key_positions(self) -> dict[str, Position]:
        return NUMPAD_POSITIONS if self == KeypadType.NUMPAD else DIRPAD_POSITIONS

NUMPAD = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A'],
]
NUMPAD_POSITIONS = {char: Position(x, y) for y, row in enumerate(NUMPAD) for x, char in enumerate(row)}
DIRPAD = [
    [' ', '^', 'A'],
    ['<', 'v', '>'],
]
DIRPAD_POSITIONS = {char: Position(x, y) for y, row in enumerate(DIRPAD) for x, char in enumerate(row)}

@cache
def find_shortest_sequence(code: str, depth: int, keypad_type: KeypadType) -> int:
    sequences = keypad_control_sequences(code, keypad_type, 'A')
    if depth == 0:
        return min(sum(len(part) for part in sequence) for sequence in sequences)
    else:
        return min(sum(find_shortest_sequence(dircode, depth - 1, KeypadType.DIRPAD) for dircode in sequence) for sequence in sequences)

def keypad_control_sequences(code: str, keypad_type: KeypadType, start: str) -> list[list[str]]:
    if code == '':
        return [[]]
    keypad_positions = keypad_type.key_positions()
    position = keypad_positions[start]
    next_position = keypad_positions[code[0]]
    dist = keypad_positions[' ']

    options = get_move_options(position, next_position, dist)
    sequences = keypad_control_sequences(code[1:], keypad_type, code[0])
    result = []
    for option in options:
        for sequence in sequences:
            result.append([option, *sequence])
    return result

def get_move_options(position: Position, next_position: Position, dist: Position) -> Iterator[str]:
    horizontal_arrow = '<' if next_position.x < position.x else '>'
    vertical_arrow = '^' if next_position.y < position.y else 'v'
    horizontal_distance = abs(position.x - next_position.x)
    vertical_distance = abs(position.y - next_position.y)

    if position == next_position:
        yield 'A'
    elif position.x == next_position.x:
        yield vertical_arrow * vertical_distance + 'A'
    elif position.y == next_position.y:
        yield horizontal_arrow * horizontal_distance + 'A'
    else:
        if not ((dist.x == next_position.x and dist.y in get_range(position.y, next_position.y)) or (dist.y == position.y and dist.x in get_range(next_position.x, position.x))):
            yield horizontal_arrow * horizontal_distance + vertical_arrow * vertical_distance + 'A'
        if not ((dist.x == position.x and dist.y in get_range(next_position.y, position.y)) or (dist.y == next_position.y and dist.x in get_range(position.x, next_position.x))):
            yield vertical_arrow * vertical_distance + horizontal_arrow * horizontal_distance + 'A'

def get_range(start: int, end: int) -> range:
    if start < end:
        return range(start, end)
    else:
        return range(start, end, -1)

input_codes = open('../inputs/input21.txt').read().splitlines()
print('Part 1:', sum([int(code[:-1]) * find_shortest_sequence(code, 2, KeypadType.NUMPAD) for code in input_codes]))
print('Part 2:', sum([int(code[:-1]) * find_shortest_sequence(code, 25, KeypadType.NUMPAD) for code in input_codes]))