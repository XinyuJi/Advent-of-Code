with open('6.txt', 'r') as file:
    map = file.read().splitlines()

directions = [(-1,0), (0,1), (1,0), (0,-1)]

def find_start_point(map):
    for i, rows in enumerate(map):
        for j, cols in enumerate(rows):
            if cols == "^":
                return(i, j)

def bfs_guard_patrol(start, map, row, col):
    visited = set()
    cx, cy = start
    cur_dir = 0
    while 0 <= cx < rows and 0 <= cy < cols:
        cur_index = cur_dir
        nx, ny = cx + directions[cur_dir][0], cy + directions[cur_dir][1]
        while 0 <= nx < rows and 0 <= ny < cols and (map[nx][ny] == "#" or(nx, ny) == (row, col)):
            cur_dir = (cur_dir + 1) % 4
            nx, ny = cx + directions[cur_dir][0], cy + directions[cur_dir][1]
        visited.add(((cx, cy), cur_index))
        cx, cy = nx, ny
        if ((nx, ny), cur_dir) in visited:
            return True
    return False

rows, cols = len(map), len(map[0])
start = find_start_point(map)

total = 0
for row in range(rows):
    for col in range(cols):
        if bfs_guard_patrol(start, map, row, col):
            print(row, col)
            total += 1
print(total)
