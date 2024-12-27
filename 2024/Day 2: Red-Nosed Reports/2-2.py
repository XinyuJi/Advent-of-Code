with open('2.txt', 'r') as file:
    lines = file.read().splitlines()
rows = [tuple(map(int, line.split())) for line in lines]

def is_valid(sequence):
    return (
        all(1 <= sequence[i] - sequence[i - 1] <= 3 for i in range(1, len(sequence))) or
        all(1 <= sequence[i - 1] - sequence[i] <= 3 for i in range(1, len(sequence)))
    )

check = 0
for row in rows:
    if is_valid(row):
        check += 1
    else:
        if any(is_valid(row[:i] + row[i+1:]) for i in range(len(row))):
            check += 1
print(check)
