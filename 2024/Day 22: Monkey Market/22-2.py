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

def record_price_changes(secret_numbers_list):
    price_changes = [{} for _ in range(len(secret_numbers_list))]
    valid_changes = set()
    for i, number in enumerate(secret_numbers_list):
        changes = (None, None, None, None)
        for _ in range(2000):
            curr_last_digit = number % 10
            next_number = generate_next_secret_number(number)
            next_num_last_digit = next_number % 10
            price_diff = next_num_last_digit - curr_last_digit
            changes = (changes[1], changes[2], changes[3], price_diff)

            if changes not in price_changes[i]:
                price_changes[i][changes] = next_num_last_digit
            valid_changes.add(changes)
            number = next_number
    return price_changes, valid_changes

price_changes, valid_changes = record_price_changes(secret_numbers_list)
max_banana = 0
for change in valid_changes:
    cur_banana = 0
    for price_change in price_changes:
        cur_banana += price_change.get(change, 0)
    if cur_banana > max_banana:
        max_banana = cur_banana
        best_change = change
print(max_banana, best_change)
