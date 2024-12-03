import re


with open('test.txt', 'r') as file:
    data = file.read()
lines = data.splitlines()

def mul(a, b):
    return a * b

result = 0
check = 0
for line in lines:  
    matches = re.findall(r"mul\(\d+,\d+\)|don\'t|do", line)
    print(matches)

    for i in matches:
        if i == "don't":
            check = 1
            continue
        if i == 'do':
            check = 0
            continue
        if check ==1:
            continue
        result += eval(i)
            
print(result)
