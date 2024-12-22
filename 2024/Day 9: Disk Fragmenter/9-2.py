with open('9.txt', 'r') as file:
    disk_map = [int(x) for x in file.read().strip()]

def create_strip(disk_map):
    strip = []  
    gaps = []  
    blocks = []
    block_id = 0
    for i, data in enumerate(disk_map):
        if i % 2 == 0:
            blocks.append((len(strip), block_id, data))
            strip.extend([block_id] * data)
            block_id += 1
        else:
            gaps.append((data, len(strip)))
            strip.extend([None] * data)
    return strip, blocks, gaps

def move_blocks(strip, blocks, gaps):
    for position, block_id, length in reversed(blocks):
        for gap_index, (gap_length, gap_position) in enumerate(gaps):
            if gap_position > position:
                break

            if gap_length >= length:
                for i in range(length):
                    strip[position + i] = None
                    strip[gap_position + i] = block_id

                remaining_gap = gap_length - length
                if remaining_gap > 0:
                    gaps[gap_index] = (remaining_gap, gap_position + length)
                else:
                    gaps.pop(gap_index)
                break

strip, blocks, gaps = create_strip(disk_map)
move_blocks(strip, blocks, gaps)
checksum = 0
for i, val in enumerate(strip):
    if val:
        checksum += val * i
print(checksum)
