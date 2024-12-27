from collections import deque

with open('4.txt', 'r') as file:
    map = file.read().splitlines()

word = "XMAS"
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def find_start_points(map, rows, cols):
    start_points = []
    for row in range(rows):
        for col in range(cols):
            if map[row][col] == "X":
                start_points.append((row, col))
    return start_points

def bfs_find_xmas(map, start, rows, cols):
    count_xmas = 0
    for dx, dy in directions:
        queue = deque([(start, 0, [start])])
        visited = set()
        while queue:
            (cx, cy), idx, path = queue.popleft()
            if idx == len(word):
                count_xmas += 1
                break
            if not (0 <= cx < rows and 0 <= cy < cols) or (cx, cy) in visited:
                continue
            if map[cx][cy] != word[idx]:
                continue

            visited.add((cx, cy))
            next_cx, next_cy = cx + dx, cy + dy
            queue.append(((next_cx, next_cy), idx + 1, path + [(next_cx, next_cy)]))
    return count_xmas

rows, cols = len(map), len(map[0])
start_points = find_start_points(map, rows, cols)

total = 0
for start in start_points:
    total += bfs_find_xmas(map, start, rows, cols)
print(f"Total Xmas found: {total}")
