from collections import deque

with open('4.txt', 'r') as file:
    data = file.read()
map = data.splitlines()

directions = [((-1, -1),((-1, 1))),((1, 1),(1, -1))]

def find_start_points(map, rows, cols):
    start_points = []
    for row in range(rows):
        for col in range(cols):
            if map[row][col] == "A":
                start_points.append((row, col))
    return start_points

def bfs_find_x_shapes(grid, start, rows, cols):
    x, y = start
    count = 0
    path1, path2 = "", ""
    positions1, positions2 = [], []
    for (dir1, dir2) in directions:
        dx1, dy1 = dir1
        dx2, dy2 = dir2
        nx1, ny1 = x + dx1, y + dy1
        nx2, ny2 = x + dx2, y + dy2

        if 0 <= nx1 < rows and 0 <= ny1 < cols:
            path1 += grid[nx1][ny1]
            positions1.append((nx1, ny1))
        if 0 <= nx2 < rows and 0 <= ny2 < cols:
            path2 += grid[nx2][ny2]
            positions2.append((nx2, ny2))

    if path1 in ("MS", "SM") and path2 in ("MS", "SM"):
        count += 1
    return count

rows, cols = len(map), len(map[0])
start_points = find_start_points(map, rows, cols)

total = 0
for start in start_points:
    total += bfs_find_x_shapes(map, start, rows, cols)
print(f"Total Xmas found: {total}")
