from collections import deque

with open('17.txt', 'r') as file:
    data = file.read()
register, program = data.strip().split("\n\n")

def get_register_value(register):
    register_dict = {}
    for r in register.splitlines():
        name, value = r.split(': ')
        register_dict[name] = int(value)
    return register_dict['Register A'], register_dict['Register B'], register_dict['Register C']

def combo(operand, a, b, c):
    return operand if operand < 4 else [a, b, c][operand - 4]

def operation(program, a, b, c, output):
    i = 0
    while i >= 0 and i < len(program):
        command = program[i]
        operand = program[i + 1]
        combo_result = combo(operand, a, b, c)
        
        if command == 0:
            a = a // (2 ** combo_result)
        elif command == 1:
            b ^= operand
        elif command == 2:
            b = combo_result % 8
        elif command == 3 and a != 0:
            i = operand
            continue
        elif command == 4:
            b ^= c
        elif command == 5:
            output.append(combo_result % 8)
        elif command == 6:
            b = a // (2 ** combo_result)
        elif command == 7:
            c = a // (2 ** combo_result)
        i += 2
    return output

def find_match(b, c, program):
    queue = deque([0])
    step = 0 
    while queue:
        step += 1
        expected_output = program[len(program) - step:]
        next_queue = deque()
        for current_value in queue:
            for digit in range(8):
                next_value = (current_value << 3) | digit
                output = []
                operation(program, next_value, b, c, output)
                if output == expected_output:
                    if step == len(program):
                        return next_value
                    next_queue.append(next_value)
        queue = next_queue

a, b, c = get_register_value(register)
program = [int(num) for num in program.split(': ')[1].split(',')]
a_value = find_match(b, c, program)
print(a_value)
