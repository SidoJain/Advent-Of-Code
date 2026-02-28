def next_blink(data: list[str]) -> list[str]:
    new_data = []
    for i in data:
        if i == '0':
            new_data.append('1')
        elif len(i) % 2 == 0:
            new_data.append(str(int(i[0:len(i) // 2])))
            new_data.append(str(int(i[len(i) // 2:])))
        else:
            new_data.append(str(int(i) * 2024))
    return new_data

def get_count(data: list[str]) -> int:
    for _ in range(25):
        data = next_blink(data)
    return len(data)

raw_input = open('../inputs/input11.txt').read().strip().replace('\n', '').split(' ')
print(get_count(raw_input))