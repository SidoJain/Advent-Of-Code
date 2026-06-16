import functools

def parseInput(filename: str) -> list[tuple[str, tuple[int, ...]]]:
    parsed_data = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                record, groups_str = line.split()
                unfolded_record = '?'.join([record] * 5)
                original_groups = [int(x) for x in groups_str.split(',')]
                unfolded_groups = tuple(original_groups * 5)
                parsed_data.append((unfolded_record, unfolded_groups))
    return parsed_data

@functools.lru_cache(maxsize=None)
def countArrangements(record: str, groups: tuple[int, ...]) -> int:
    if not record:
        return 1 if not groups else 0
    if not groups:
        return 0 if '#' in record else 1

    char = record[0]
    total_arrangements = 0
    if char in '.?':
        total_arrangements += countArrangements(record[1:], groups)
    if char in '#?':
        group = groups[0]
        if (len(record) >= group and '.' not in record[:group] and (len(record) == group or record[group] != '#')):
            total_arrangements += countArrangements(record[group + 1:], groups[1:])
    return total_arrangements

data = parseInput('../inputs/input12.txt')
print(sum(countArrangements(record, groups) for record, groups in data))