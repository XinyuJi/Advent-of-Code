from collections import deque

with open('18.txt', 'r') as file:
    data = file.read()
bytes_list = [tuple(map(int, line.split(','))) for line in data.strip().split('\n')]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start = (0,0)

def bfs_find_path(obstacles, len_space, end):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end:
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx <= len_space and 0 <= ny <= len_space and 
               (nx, ny) not in obstacles and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

def min_steps_to_exit(pos_list, len_space, end):
    obstacles = set()
    for x, y in pos_list:
        obstacles.add((x, y))
    steps = bfs_find_path(obstacles, len_space, end)
    return steps

len_space = 70
end = (len_space, len_space)
steps = min_steps_to_exit(bytes_list[:1024], len_space, end)
print(steps)
