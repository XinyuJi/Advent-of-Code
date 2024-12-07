with open('test.txt', 'r') as file:
    data = file.read()
map = data.splitlines()

word = "XMAS"
directions = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(-1, -1),(1, -1),(-1, 1)]

result = []
for row in range(len(map)):
    for col in range(len(map[0])):
        for dir in directions:
            row_step, col_step = dir
            check = 0
            for i in range(len(word)):
                r, c = row + i*row_step, col + i *col_step
                if not (0 <= r < len(map) and 0 <= c < len(map[0])):
                    check = 1
                    break
                if map[r][c] != word[i]:
                    check = 1
                    break
            if check == 0:
                result.append(((row, col), dir))
print(result)
print(len(result))
