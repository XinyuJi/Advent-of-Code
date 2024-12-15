import re

def parse_file(file_path):
    groups = []
    each_group = {}

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            match_a = re.match(r'Button A: X\+(\d+), Y\+(\d+)', line)
            if match_a:
                each_group['A'] = (int(match_a.group(1)), int(match_a.group(2)))
                continue
            
            match_b = re.match(r'Button B: X\+(\d+), Y\+(\d+)', line)
            if match_b:
                each_group['B'] = (int(match_b.group(1)), int(match_b.group(2)))
                continue

            match_prize = re.match(r'Prize: X=(\d+), Y=(\d+)', line)
            if match_prize:
                each_group['P'] = (int(match_prize.group(1)), int(match_prize.group(2)))
                groups.append(each_group)
                each_group = {}
    return groups

def solve_equation(ax, ay, bx, by, px, py):
    D = ax * by - ay * bx
    Dx = px * by - py * bx
    Dy = ax * py - ay * px
    x = Dx / D
    y = Dy / D
    return x, y

def is_integer(value):
    return value % 1 == 0

data = parse_file('13.txt')
coins = 0
for i, group in enumerate(data):
    ax, ay = group['A']
    bx, by = group['B']
    px, py = group['P']
    press_a, press_b = solve_equation(ax, ay, bx, by, px, py)
    if press_a < 100 and press_b <100 and is_integer(press_a) and is_integer(press_b):
        press_a, press_b = int(press_a), int(press_b)
        coins += 3*int(press_a) + int(press_b)
print(coins)
