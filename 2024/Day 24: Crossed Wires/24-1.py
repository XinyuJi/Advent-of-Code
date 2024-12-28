with open('24.txt', 'r') as file:
    wire, operations = file.read().split('\n\n')

def phrase_wire_and_operations():
    wire_dict = {}
    for line in wire.strip().splitlines():
        key, value = line.split(':')
        wire_dict[key.strip()] = int(value.strip())

    operations_list = []
    for line in operations.strip().splitlines():
        operand1, operator, operand2, _, result = line.split(" ")
        operations_list.append((operand1, operator, operand2, result))
    return wire_dict, operations_list

def perform_operation(operator, operand1, operand2):
    if operator == "AND":
        return operand1 & operand2
    elif operator == "OR":
        return operand1 | operand2
    elif operator == "XOR":
        return operand1 ^ operand2

def gate_connection(wire_dict, operations_list):
    while operations_list:
        for i, (operand1, operator, operand2, result) in enumerate(operations_list):
            operand1_value = wire_dict[operand1] if operand1 in wire_dict else None
            operand2_value = wire_dict[operand2] if operand2 in wire_dict else None
            if operand1_value is None or operand2_value is None:
                continue
            wire_dict[result] = perform_operation(operator, operand1_value, operand2_value)
            operations_list.pop(i)
    return wire_dict

def form_new_number(wire_dict):
    sorted_keys = sorted([key for key in wire_dict.keys() if key.startswith('z')])
    values = [wire_dict[key] for key in sorted_keys]
    reversed_values = values[::-1]
    binary_string = "".join(map(str, reversed_values))
    return binary_string, len(binary_string)

wire_dict, operations_list = phrase_wire_and_operations()
wire_dict = gate_connection(wire_dict, operations_list)
new_number = form_new_number(wire_dict)
print(new_number)
