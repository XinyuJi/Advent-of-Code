with open('9.txt', 'r') as file:
    disk_map = [int(x) for x in file.read().strip()]

def create_strip(disk_map):
    strip = []
    block_id = 0
    for i, data in enumerate(disk_map):
        if i % 2 == 0:
            strip.extend([block_id] * data)
            block_id += 1
        else:
            strip.extend([None] * data)
    return strip

def move_data(strip):
    free_space = strip.index(None)
    for i, data in reversed(list(enumerate(strip))):
        if data:
            strip[free_space] = data
            strip[i] = None
            while free_space < len(strip) and strip[free_space]:
                free_space += 1
            if i - free_space <= 1:
                break
    return strip

strip = create_strip(disk_map)
strip = move_data(strip)
checksum = 0
for i, val in enumerate(strip):
    if val:
        checksum += val * i
print(checksum)
