from itertools import product

def evaluate_expression(nums, operators):
    result = nums[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += nums[i + 1]
        elif op == '*':
            result *= nums[i + 1]
    return result

def can_form_target(target, nums):
    operators = list(product(['+', '*'], repeat=len(nums) - 1))
    for ops in operators:
        if evaluate_expression(nums, ops) == target:
            return True
    return False

with open('test.txt', 'r') as file:
    data = file.read()
data_dict = {}
lines = data.strip().split("\n")
for line in lines:
    key, values = line.split(":")
    data_dict[int(key)] = list(map(int, values.split()))

total = 0
for target, nums in data_dict.items():
    if can_form_target(target, nums):
        total += target
print(total)
