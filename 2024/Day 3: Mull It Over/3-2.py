import re

with open('3.txt', 'r') as file:
    lines = file.read().splitlines()

def mul(a, b):
    return a * b

result = 0
check = False
pattern = re.compile(r"mul\(\d+,\d+\)|don't|do")
for line in lines:  
    matches = pattern.findall(line)
    for match in matches:
        if match == "don't":
            check = True
        elif match == 'do':
            check = False
        elif not check:
            numbers = re.findall(r'\d+', match)
            a, b = map(int, numbers)
            result += mul(a, b)
print(result)
