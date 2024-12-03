import re


with open('test.txt', 'r') as file:
    data = file.read()
lines = data.splitlines()

def mul(a, b):
    return a * b

result = 0
for line in lines:  
    print(line)
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    print(matches)
    for i in matches:
        result += eval(i)
print(result)
