
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
    values = [[{
        ">": (math.inf, set()),
        "v": (math.inf, set()),
        "<": (math.inf, set()),
        "^": (math.inf, set())
    } for _ in range(cols)] for _ in range(rows)]
    queue = deque([(*start, ">", 0, set([start]))])
    while queue:
        cx, cy, direction, cost, path = queue.popleft()
        if not (0 <= cx < rows and 0 <= cy < cols) or map[cx][cy] == '#':
            continue
        path.add((cx, cy))

        cur_min, cur_path = values[cx][cy][direction]
        if cur_min < cost:
            continue
        elif cur_min == cost:
            cur_path.update(path)
        else:
            cur_path.clear()
            cur_path.update(path)
            values[cx][cy][direction]=(cost, cur_path)
        if cur_min > cost:
            values[cx][cy][direction] = (cost, set(path))
        else:
            cur_path.update(path)
        if (cx, cy) == end:
            continue
        
        rotate, delta = directions[direction]
        queue.append([cx + delta[0], cy + delta[1], direction, cost + 1, set(path)])
        for r in rotate:
            queue.append([cx, cy, r, cost + 1000, set(path)])
    return values[end[0]][end[1]]

start, end = find_start_and_end(map)
score = bfs_find_path(map, start, end)
final_path = min(score.items(), key=lambda x: x[1][0])[1][1]
print(len(final_path))
