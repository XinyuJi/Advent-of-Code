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

def operation(program, a, b, c):
    output = []
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

a, b, c = get_register_value(register)
program = [int(num) for num in program.split(': ')[1].split(',')]
output = operation(program, a, b, c)
output = ",".join(map(str, output))
print(output)
