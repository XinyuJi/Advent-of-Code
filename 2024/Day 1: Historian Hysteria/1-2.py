with open("1.txt", 'r') as file:
    data = file.read()
lines = data.splitlines()
rows = [tuple(map(int, line.split())) for line in lines]

count_dict = {row[0]: 0 for row in rows}
for row in rows:
    if row[1] in count_dict:
        count_dict[row[1]] += 1

score = 0
for i in range(len(rows)):
    left = rows[i][0]
    score += left * count_dict[left]
print(score)
