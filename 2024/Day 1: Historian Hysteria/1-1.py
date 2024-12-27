with open("1.txt", 'r') as file:
    lines = file.read().splitlines()
rows = [tuple(map(int, line.split())) for line in lines]

sorted_by_first = sorted(rows, key=lambda x: x[0])
sorted_by_second = sorted(rows, key=lambda x: x[1])

total_distance = 0
for i in range(len(rows)):
    total_distance += abs(sorted_by_first[i][0] - sorted_by_second[i][1])
print(total_distance)
