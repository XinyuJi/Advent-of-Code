from collections import deque

with open('10.txt', 'r') as file:
    data = file.read()
map = data.splitlines()

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_start_points(map, rows, cols):
    start_points = []
    for row in range(rows):
        for col in range(cols):
            if "0" == map[row][col]:
                start_points.append((row, col))
    return start_points

def bfs_hiking_trails(map, start, rows, cols):
    queue = deque([(start, "0")])
    paths = 0
    visited = set()
    while queue:
        (cx, cy), current_path = queue.popleft()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        if current_path == "0123456789":
            paths += 1
            continue

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                next_value = map[nx][ny]
                if next_value == str(int(current_path[-1]) + 1):
                    queue.append(((nx, ny), current_path + next_value))
    return paths

scores = 0
rows, cols = len(map), len(map[0])
start_points = find_start_points(map, rows, cols)

for start in start_points:
    scores += bfs_hiking_trails(map, start, rows, cols)
print(f"Sum of the scores of all trailheads: {scores}")
