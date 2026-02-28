def calculate_next_secret(secret: int) -> int:
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

def find_2000th_secret(secret: int) -> int:
    for _ in range(2000):
        secret = calculate_next_secret(secret)
    return secret

secrets = [int(secret) for secret in open('../inputs/input22.txt').read().splitlines()]
result = sum(find_2000th_secret(secret) for secret in secrets)
print(result)