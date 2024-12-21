from collections import deque

with open('18.txt', 'r') as file:
    data = file.read()
bytes_list = [tuple(map(int, line.split(','))) for line in data.strip().split('\n')]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start = (0, 0)

def bfs_can_reach_end(obstacles, len_space, end):
    queue = deque([start])
    visited = {start}
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx <= len_space and 0 <= ny <= len_space and 
                (nx, ny) not in obstacles and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False

def find_first_unreachable_point(bytes_list, len_space, end):
    obstacles = set()
    for x, y in bytes_list:
        obstacles.add((x, y))
        if not bfs_can_reach_end(obstacles, len_space, end):
            return (x, y)
    return None

len_space = 70
end = (len_space, len_space)
first_unreachable = find_first_unreachable_point(bytes_list, len_space, end)
print(first_unreachable)
