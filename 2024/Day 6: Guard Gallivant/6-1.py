with open('6.txt', 'r') as file:
    data = file.read()
map = data.splitlines()

directions = [(-1,0), (0,1), (1,0), (0,-1)]

def find_start_point(map):
    for i, rows in enumerate(map):
        for j, cols in enumerate(rows):
            if cols == "^":
                return(i, j)

def bfs_guard_patrol(start, map):
    visited = set()
    rows, cols = len(map), len(map[0])
    cx, cy = start
    cur_dir = 0
    while 0 <= cx < rows and 0 <= cy < cols:
        nx, ny = cx + directions[cur_dir][0], cy + directions[cur_dir][1]
        while 0 <= nx < rows and 0 <= ny < cols and map[nx][ny] == "#":
            cur_dir = (cur_dir + 1) % 4
            nx, ny = cx + directions[cur_dir][0], cy + directions[cur_dir][1]
        visited.add((cx, cy))
        cx, cy = nx, ny
    return visited

start = find_start_point(map)
visted_pos = bfs_guard_patrol(start, map)
print(len(visted_pos))
