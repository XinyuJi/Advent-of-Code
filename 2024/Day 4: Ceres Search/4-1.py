with open('test.txt', 'r') as file:
    data = file.read()
grid = data.splitlines()

word = "XMAS"
word_length = len(word)

directions = [
    (0, 1),    # Right
    (0, -1),   # Left
    (1, 0),    # Down
    (-1, 0),   # Up
    (1, 1),    # Down-Right
    (-1, -1),  # Up-Left
    (1, -1),   # Down-Left
    (-1, 1)    # Up-Right
]

def search_direction(grid, word, row, col, direction):
    row_step, col_step = direction
    for i in range(word_length):
        r, c = row + i * row_step, col + i * col_step
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            return False
        if grid[r][c] != word[i]:
            return False
    return True

def find_word(grid, word):
    results = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for direction in directions:
                if search_direction(grid, word, row, col, direction):
                    results.append(((row, col), direction))
    return results


matches = find_word(grid, word)
print(len(matches))

# for match in matches:
#     start, direction = match
#     print(f"Found 'XMAS' starting at {start} in direction {direction}")
