import re

with open('3.txt', 'r') as file:
    lines = file.read().splitlines()

def mul(a, b):
    return a * b

result = 0
pattern = re.compile(r'mul\((\d+),(\d+)\)')
for line in lines:
    matches = pattern.findall(line)
    for match in matches:
        a, b = map(int, match)
        result += mul(a, b)
print(result)
