with open('15.txt', 'r') as file:
    data = file.read()
map, rules = data.strip().split("\n\n")
map = map.splitlines()
rules = list(''.join([rule.strip() for rule in rules.split() if rule.strip()]))

directions = {">": (0,1), "<": (0,-1), "^": (-1,0), "v": (1,0)}

def get_wider_map(map):
    char_map = {
        "#": ["#", "#"],
        "O": ["[", "]"],
        ".": [".", "."],
        "@": ["@", "."]
    }
    wider_map = []
    for row in map:
        new_row = []
        for col in row:
            new_row.extend(char_map.get(col, [col]))
        wider_map.append(new_row)
    return wider_map

def find_start_point(map):
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == "@":
                return (row, col)

def check_movable(map, cx, cy, dx, dy, visited):
    if (cx, cy) in visited:
        return True
    visited.add((cx, cy))
    nx, ny = cx + dx, cy + dy
    current_cell = map[nx][ny]
    if current_cell == "#":
        return False
    elif current_cell == "O":
        return check_movable(map, nx, ny, dx, dy, visited)
    elif current_cell == "[":
        return check_movable(map, nx, ny, dx, dy, visited) and check_movable(map, nx, ny + 1, dx, dy, visited)
    elif current_cell == "]":
        return check_movable(map, nx, ny, dx, dy, visited) and check_movable(map, nx, ny - 1, dx, dy, visited)
    return True

def robot_moves(map, cx, cy, rule):
    dx, dy = directions[rule]
    nx, ny = cx + dx, cy + dy
    if not (0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] != "#"):
        return cx, cy
    if map[nx][ny] in ["[", "]", "O"]:
        visited = set()
        if not check_movable(map, cx, cy, dx, dy, visited):
            return cx, cy
        while visited:
            for x, y in visited.copy():
                nx2, ny2 = x + dx, y + dy
                if (nx2, ny2) not in visited:
                    if map[nx2][ny2] != "@" and map[x][y] != "@":
                        map[nx2][ny2] = map[x][y]
                        map[x][y] = "."
                    visited.remove((x, y))
        map[cx][cy], map[nx][ny] = map[nx][ny], map[cx][cy]
        return nx, ny
    map[cx][cy], map[nx][ny] = map[nx][ny], map[cx][cy]
    return nx, ny

def gps_coordinate(map):
    total = 0
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] in ["O", "["]:
                total += 100 * row + col
    return total

wider_map = get_wider_map(map)
row, col = find_start_point(wider_map)
total = 0
for rule in rules:
    row, col = robot_moves(wider_map, row, col, rule)
total = gps_coordinate(wider_map)
print(total)
