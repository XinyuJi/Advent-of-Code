with open("1.txt", 'r') as file:
        data = file.read()

lines = data.splitlines()
rows = [tuple(map(int, line.split())) for line in lines]

dict = {}
for i in range(len(rows)):
    left = rows[i][0]
    if left not in dict:
        dict[left] = 0

for i in range(len(rows)):
    right = rows[i][1]
    if right in dict:
        dict[right] += 1

score = 0
for i in range(len(rows)):
    left = rows[i][0]
    score += left * dict[left]

print(score)
