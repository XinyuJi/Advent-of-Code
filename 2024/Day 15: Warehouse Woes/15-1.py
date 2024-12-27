with open('15.txt', 'r') as file:
    map, rules = file.read().strip().split("\n\n")
map = map.splitlines()
rules = [rule.strip() for rule in rules.split() if rule.strip()]
rules = list(''.join(rules))

directions = {">": (0,1), "<": (0,-1), "^": (-1,0), "v": (1,0)}

def find_start_point(map, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if map[row][col] == "@":
                return (row, col)

def robot_moves(start, rows, cols, map):
    cx, cy = start
    new_map = [list(row) for row in map]
    for rule in rules:
        rx, ry = directions[rule]
        nx, ny = cx + rx, cy + ry
        fx, fy = nx, ny
        while new_map[fx][fy] == "O":
            fx, fy = fx + rx, fy + ry
        if new_map[fx][fy] != "#":
            new_map[fx][fy] = new_map[nx][ny]
            new_map[nx][ny] = "@"
            cx, cy = nx, ny
    return new_map

def gps_coordinate(map, rows, cols):
    total = 0
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == "O":
                total += 100 * i + j
    return total

rows, cols = len(map), len(map[0])
start = find_start_point(map, rows, cols)
new_map = robot_moves(start, rows, cols, map)
total = gps_coordinate(new_map, rows, cols)
print(total)
