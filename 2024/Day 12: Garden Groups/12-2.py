from collections import deque

with open('12.txt', 'r') as file:
    map = file.read().splitlines()

rows, cols = len(map), len(map[0])
border_check = {'^': ((0, -1), (0, 1)), '>': ((1, 0), (-1, 0)), 'v': ((0, 1), (0, -1)), '<': ((-1, 0), (1, 0))}
directions = {(-1, 0): '^', (0, -1): '<', (1, 0): 'v', (0, 1): '>'}
dir_pos = list(directions.keys())

def find_sides(borders):
    sides = 0
    for key in borders:
        border_points = set(borders[key])
        while border_points:
            cur_point = border_points.pop()
            for move_dir in border_check[key]:
                next_point = (cur_point[0] + move_dir[0], cur_point[1] + move_dir[1])
                while next_point in border_points:
                    border_points.remove(next_point)
                    next_point = (next_point[0] + move_dir[0], next_point[1] + move_dir[1])
            sides += 1
    return sides

def bfs_flood_fill(map, start, visited):
    start_value = map[start[0]][start[1]]
    area, perimeter = 0, 0
    queue = deque([start])
    borders = {key: set() for key in directions.values()}
    while queue:
        cx, cy = queue.popleft()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1
        for dx, dy in dir_pos:
            nx, ny = cx + dx, cy + dy
            dir_sym = directions[(dx, dy)]
            if not (0 <= nx < rows and 0 <= ny < cols):
                borders[dir_sym].add((cx, cy))
            elif map[nx][ny] != start_value:
                borders[dir_sym].add((cx, cy))
            else:
                queue.append((nx, ny))
    return area, borders

result = 0
visited = set()
for row in range(rows):
    for col in range(cols):
        if (row, col) not in visited:
            area, borders = bfs_flood_fill(map, (row, col), visited)
            sides = find_sides(borders)
            result += area * sides
print(result)
