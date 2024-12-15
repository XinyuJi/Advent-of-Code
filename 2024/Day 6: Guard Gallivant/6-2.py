with open('test.txt', 'r') as file:
    data = file.read()
map = data.splitlines()
rows, cols = len(map[0]), len(map)
directions = [(-1,0), (0,1), (1,0), (0,-1)]

def find_start(map):
    for i, rows in enumerate(map):
        for j, cols in enumerate(rows):
            if cols == "^":
                return(i, j)

def walk(start, map, i, j):
    visited = set()
    cx, cy = start
    cur_dir = 0
    while 0 <= cx < rows and 0 <= cy < cols:
        cur_index = cur_dir
        nx, ny = cx + directions[cur_dir][0], cy + directions[cur_dir][1]
        while 0 <= nx < rows and 0 <= ny < cols and (map[nx][ny] == "#" or(nx,ny) == (i,j)):
            cur_dir = (cur_dir + 1) % 4
            nx, ny = cx + directions[cur_dir][0], cy + directions[cur_dir][1]
        visited.add(((cx, cy), cur_index))
        cx, cy = nx, ny
        if ((nx, ny), cur_dir) in visited:
            return True
    return False

start = find_start(map)
total = 0
for i in range(rows):
    for j in range(cols):
        if walk(start, map, i, j):
            total += 1
            print(i, j)
print(total)
