from collections import defaultdict

with open('8.txt','r') as file:
    map = file.read().splitlines()

def extract_antennas(map):
    antennas = defaultdict(list)
    for y, row in enumerate(map):
        for x, col in enumerate(row):
            if col != ".":
                antennas[col].append((x, y))
    return antennas

def find_antinodes(antennas, rows, cols):
    antinodes = set()
    for ante, pos in antennas.items():
        num_ante = len(pos)
        for i in range(num_ante):
            for j in range(i+1, num_ante):
                x1, y1 = pos[i]
                x2, y2 = pos[j]
                dx, dy = x2 - x1, y2 - y1
                ax, ay = x1 - dx, y1 - dy
                bx, by = x2 + dx, y2 + dy
                for (qx, qy) in [(ax, ay), (bx, by)]:
                    if 0 <= qx < rows and 0 <= qy < cols:
                        antinodes.add((qx, qy))
    return antinodes

def mark_antinodes(map, antinodes, antennas):
    map = [list(row) for row in map]
    count = 0
    antenna_positions = {pos for positions in antennas.values() for pos in positions}
    for x, y in antinodes:
        if map[y][x] == "." or (x, y) in antenna_positions:
            map[y][x] = "#"
            count += 1
    return ["".join(row) for row in map], count

antennas = extract_antennas(map)
rows, cols = len(map), len(map[0])
antinodes = find_antinodes(antennas, rows, cols)
new_map, antinode_count = mark_antinodes(map, antinodes, antennas)

print(f"Number of antinodes: {antinode_count}")
for line in new_map:
    print(line)
