with open('25.txt', 'r') as file:
    data = file.read()
blocks = data.split('\n\n')

def find_locks_and_keys(block_list, key, lock):
    rows = len(block_list)
    cols = len(block_list[0])
    hash_set = [0] * cols
    for row in block_list:
        for col, char in enumerate(row):
            if char == '#':
                hash_set[col] += 1

    if '#' in block_list[0]:
        key.append(hash_set)
    else:
        lock.append(hash_set)
    return key, lock

def process_blocks(blocks):
    key, lock = [], []
    for block in blocks:
        block_list = block.strip().split('\n')
        find_locks_and_keys(block_list, key, lock)
    return key, lock

def find_match(key, lock):
    return len(key) == len(lock) and all(k + l <= 7 for k, l in zip(key, lock))

key, lock = process_blocks(blocks)
match = 0
for k in key:
    for l in lock:
        if find_match(k, l):
            match += 1
print(match)
