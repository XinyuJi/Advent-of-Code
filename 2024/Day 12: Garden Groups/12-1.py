from collections import deque

with open('12.txt', 'r') as file:
    map = file.read().splitlines()

rows, cols = len(map), len(map[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs_flood_fill(map, start, visited):
    start_value = map[start[0]][start[1]]
    area, perimeter = 0, 0
    queue = deque([start])
    while queue:
        (cx, cy) = queue.popleft() 
        if (cx, cy) in visited: 
            continue
        visited.add((cx, cy))  
        area += 1
        for dx, dy in directions:  
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < rows and 0 <= ny < cols):
                perimeter += 1
            elif map[nx][ny] != start_value:
                perimeter += 1
            else:
                queue.append((nx, ny))
    return area, perimeter

result = 0
visited = set()
for row in range(rows):
    for col in range(cols):
        if (row, col) not in visited:
            area, perimeter = bfs_flood_fill(map, (row, col), visited)
            result += area * perimeter
print(result)
