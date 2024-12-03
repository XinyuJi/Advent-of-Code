with open('2.txt', 'r') as file:
    data = file.read()

lines = data.splitlines()
rows = [tuple(map(int, line.split())) for line in lines]

check = 0
for j in range(len(rows)):
    row = rows[j]
    print(row)
    is_increasing = all(1 <= (row[i] - row[i - 1]) <= 3 for i in range(1, len(row)))
    is_decreasing = all(1 <= (row[i-1] - row[i]) <=3 for i in range(1, len(row)))
    print(is_decreasing, is_increasing)
    if (is_decreasing or is_increasing) is True:
        check += 1

print(check)
