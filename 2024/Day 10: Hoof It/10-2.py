from collections import deque

with open('10.txt', 'r') as file:
    data = file.read()
map = data.splitlines()

def find_bfs_start(map, rows, cols):
    start = []
    for row in range(rows):
        for col in range(cols):
            if "0" == map[row][col]:
                start.append((row, col))
    return start

def bfs(map, start_index, rows, cols):
    queue = deque([(start_index, "0")])
    paths = 0
    visited = set()

    while queue:
        (cx, cy), current_path = queue.popleft()
        visited.add((cx, cy))
        if current_path == "0123456789":
            paths += 1
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                next_value = map[nx][ny]
                if next_value == str(int(current_path[-1]) + 1):
                    queue.append(((nx, ny), current_path + next_value))
    return paths

final_paths = 0
rows, cols = len(map), len(map[0])
start = find_bfs_start(map, rows, cols)

for i in start:
    final_paths += bfs(map, i, rows, cols)
print(f"Total paths found: {final_paths}")
