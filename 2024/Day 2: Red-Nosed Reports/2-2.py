with open('2.txt', 'r') as file:
    data = file.read()

lines = data.splitlines()
rows = [tuple(map(int, line.split())) for line in lines]

def is_valid(sequence):
    return (
        all(1 <= sequence[i] - sequence[i - 1] <= 3 for i in range(1, len(sequence))) or
        all(1 <= sequence[i - 1] - sequence[i] <= 3 for i in range(1, len(sequence)))
    )

check = 0
j = 0
for j in range(len(rows)):
    row = rows[j]
    print(row)
    if is_valid(row):
        check += 1
        continue
    for i in range(len(row)):
        modified_row = row[:i] + row[i+1:]
        if is_valid(modified_row):
            check +=1
            break

print(check)