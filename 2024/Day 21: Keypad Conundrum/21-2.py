with open('21.txt', 'r') as file:
    codes = file.read().splitlines()

numeric_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["#", "0", "A"],
]
directional_keypad = [["#", "^", "A"], ["<", "v", ">"]]
directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

cache = {}

def find_button_position(keyboard, button):
    rows, cols = len(keyboard), len(keyboard[0])
    for row in range(rows):
        for col in range(cols):
            if keyboard[row][col] == button:
                return row, col

def generate_instructions(keyboard, start_row, start_col, end_row, end_col):
    dr, dc = end_row - start_row, end_col - start_col
    vertical_moves = "v" * dr if dr > 0 else "^" * (-dr)
    horizontal_moves = ">" * dc if dc > 0 else "<" * (-dc)
    instruction = []
    for moves in (vertical_moves + horizontal_moves, horizontal_moves + vertical_moves):
        row, col = start_row, start_col
        for move in moves:
            dr, dc = directions[move]
            row, col = row + dr, col + dc
            if keyboard[row][col] == "#":
                break
        else:
            instruction.append(moves + "A")
    return instruction

def directional_button_presses(instruction, depth):
    if depth == 0:
        return len(instruction)

    key = (tuple(instruction), depth)
    if key in cache:
        return cache[key]

    start_row, start_col = find_button_position(directional_keypad, "A")
    total_button_presses = 0
    for char in instruction:
        end_row, end_col = find_button_position(directional_keypad, char)
        instructions = generate_instructions(directional_keypad, start_row, start_col, end_row, end_col)
        total_button_presses += min(directional_button_presses(instruction, depth - 1) for instruction in instructions)
        start_row, start_col = end_row, end_col
    
    cache[key] = total_button_presses
    return total_button_presses

def get_button_presses(code, depth=25):
    start_row, start_col = find_button_position(numeric_keypad, "A")
    total = 0
    for char in code:
        end_row, end_col = find_button_position(numeric_keypad, char)
        instructions = generate_instructions(numeric_keypad, start_row, start_col, end_row, end_col)
        total += min(directional_button_presses(instruction, depth) for instruction in instructions)
        start_row, start_col = end_row, end_col
    return total

complexities = 0
for code in codes:
    num = int("".join([char for char in code if char.isdigit()]))
    button_len = get_button_presses(code)
    complexities += num * button_len
print(complexities)
