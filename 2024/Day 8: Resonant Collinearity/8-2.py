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

def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

def find_antinodes(antennas, row, col):
    antinodes = set()
    for ante, pos in antennas.items():
        num_ante = len(pos)
        for p in pos:
            antinodes.add(p)

        for i in range(num_ante):
            for j in range(i + 1, num_ante):
                x1, y1 = pos[i]
                x2, y2 = pos[j]
                dx, dy = x2 - x1, y2 - y1

                for t in [-1, 1]:
                    nx, ny = x2 + t * dx, y2 + t * dy
                    while 0 <= nx < row and 0 <= ny < col:
                        antinodes.add((nx, ny))
                        nx, ny = nx + t * dx, ny + t * dy

                for k in range(j + 1, num_ante):
                    if is_collinear(pos[i], pos[j], pos[k]):
                        antinodes.add(pos[k])
    return antinodes

def mark_antinodes(map, antinodes, antennas):
    map = [list(row) for row in map]
    count = 0
    for x, y in antinodes:
        if map[y][x] == "." or map[y][x] != ".":
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
