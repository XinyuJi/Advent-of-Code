with open('22.txt', 'r') as file:
    secret_numbers_list = [int(line.strip()) for line in file]

def mix_with_secret_number(secret_number, value):
    return secret_number ^ value

def prune_secret_number(secret_number):
    return secret_number % 16777216

def step(secret_number, multiplier, divisor=None):
    cur_value = secret_number * multiplier
    if divisor:
        cur_value //= divisor
    cur_value = mix_with_secret_number(secret_number, cur_value)
    return prune_secret_number(cur_value)

def generate_next_secret_number(secret_number):
    secret_number = step(secret_number, multiplier=64)
    secret_number = step(secret_number, multiplier=1, divisor=32)
    secret_number = step(secret_number, multiplier=2048)
    return secret_number

result = 0
for number in secret_numbers_list:
    secret_number = number
    for _ in range(2000):
        secret_number = generate_next_secret_number(secret_number)
    result += secret_number
print(result)
