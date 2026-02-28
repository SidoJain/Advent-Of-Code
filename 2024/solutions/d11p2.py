from collections import Counter

def process_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        stone_str = str(stone)
        return [int(stone_str[:mid]), int(stone_str[mid:])]
    else:
        return [stone * 2024]

def next_blink(counter: Counter) -> Counter:
    new_counter = Counter()
    for stone, count in counter.items():
        results = process_stone(stone)
        for result in results:
            new_counter[result] += count
    return new_counter

def get_count(initial_data: list[int], blinks: int) -> int:
    counter = Counter(initial_data)

    for _ in range(blinks):
        counter = next_blink(counter)
    return sum(counter.values())

raw_data = [int(x) for x in open('../inputs/input11.txt').read().strip().split()]
blinks = 75
result = get_count(raw_data, blinks)
print(result)