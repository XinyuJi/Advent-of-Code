with open('1-2.txt', 'r') as file:
    data = file.read()

lines = data.splitlines()
rows = [tuple(map(int, line.split())) for line in lines]

i = 0
dict = {}
while i < len(rows):
    l = rows[i][0]
    if l not in dict:
        dict[l] = 0
    i += 1
print(dict)

i = 0
while i < len(rows):
    r = rows[i][1]
    if r in dict:
        dict[r] += 1
    i += 1
print(dict)

sum_l = 0
for i in range(len(rows)):
    l = rows[i][0]
    sum_l += l * dict[l]


print(sum_l)