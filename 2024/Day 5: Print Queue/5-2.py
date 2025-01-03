from functools import cmp_to_key

with open('5.txt', 'r') as file:
    rules, inputs = file.read().strip().split("\n\n")

total = 0
for input in inputs.split():
    input = input.split(",")
    sort_input = sorted(input, key=cmp_to_key(lambda x, y:-(x+'|'+ y in rules)))
    if sort_input != input:
        mid = sort_input[len(sort_input)//2]
        total += int(mid)
print(total)
