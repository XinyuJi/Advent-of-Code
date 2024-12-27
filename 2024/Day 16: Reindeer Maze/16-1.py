import math
from collections import deque

with open('16.txt', 'r') as file:
    map = file.read().splitlines()

directions = {
    "^": (["<", ">"], (-1, 0)),
    ">": (["^", "v"], (0, 1)),
    "v": (["<", ">"], (1, 0)),
    "<": (["^", "v"], (0, -1))
}

def find_start_and_end(map):
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
            elif cell == "E":
                end = (i, j)
    return start, end

def bfs_find_path(map, start, end):
    rows, cols = len(map), len(map[0])
    direction_index = {"^": 0, ">": 1, "v": 2, "<": 3}
    values = [[[math.inf for _ in range(4)] for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start[0], start[1], ">", 0)])
    
    while queue:
        cx, cy, direction, cost = queue.popleft()
        if not (0 <= cx < rows and 0 <= cy < cols) or map[cx][cy] == "#":
            continue
        dir_idx = direction_index[direction]
        if values[cx][cy][dir_idx] <= cost:
            continue
        values[cx][cy][dir_idx] = cost
        if (cx, cy) == end:
            continue
        rotate, delta = directions[direction]
        nx, ny = cx + delta[0], cy + delta[1]
        queue.append((nx, ny, direction, cost + 1))
        for r in rotate:
            queue.append((cx, cy, r, cost + 1000))
    return min(values[end[0]][end[1]])

start, end = find_start_and_end(map)
score = bfs_find_path(map, start, end)
print(score)
