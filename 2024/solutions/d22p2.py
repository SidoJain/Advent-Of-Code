def calculate_next_secret(secret: int) -> int:
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

def find_max_bananas(secrets: list[int], num_prices: int = 2000) -> int:
    total = {}
    for secret in secrets:
        last = secret % 10
        pattern = []

        for _ in range(num_prices):
            secret = calculate_next_secret(secret)
            temp = secret % 10
            pattern.append((temp - last, temp))
            last = temp

        seen = set()
        for i in range(len(pattern) - 4):
            pat = tuple(x[0] for x in pattern[i:i + 4])
            val = pattern[i + 3][1]

            if pat not in seen:
                seen.add(pat)
                if pat not in total:
                    total[pat] = val
                else:
                    total[pat] += val
    return max(total.values())

secrets = [int(secret) for secret in open('../inputs/input22.txt').read().splitlines()]
max_bananas = find_max_bananas(secrets)
print(max_bananas)