with open('24.txt', 'r') as file:
    data = file.read().split('\n\n')

def phrase_wire():
    wire_dict = {}
    for line in data[0].strip().splitlines():
        key, value = line.split(':')
        wire_dict[key.strip()] = int(value.strip())
    return wire_dict

def perform_operation(operator, operand1, operand2):
    if operator == "AND":
        return operand1 & operand2
    elif operator == "OR":
        return operand1 | operand2
    elif operator == "XOR":
        return operand1 ^ operand2

def gate_connection(wire_dict):
    pending_operations = []
    for line in data[1].strip().splitlines():
        operation, result = line.split('->')
        operation = operation.strip()
        result = result.strip()
        pending_operations.append((operation, result))

    while pending_operations:
        for i, (operation, result) in enumerate(pending_operations):
            try:
                operand1, operator, operand2 = operation.split()
                operand1_value = wire_dict[operand1] if operand1 in wire_dict else None
                operand2_value = wire_dict[operand2] if operand2 in wire_dict else None
                if operand1_value is None or operand2_value is None:
                    continue
                wire_dict[result] = perform_operation(operator, operand1_value, operand2_value)
                pending_operations.pop(i)
                break
            except KeyError:
                continue
    return wire_dict

def form_new_number(wire_dict):
    sorted_keys = sorted([key for key in wire_dict.keys() if key.startswith('z')])
    values = [wire_dict[key] for key in sorted_keys]
    reversed_values = values[::-1]
    binary_string = "".join(map(str, reversed_values))
    decimal_number = int(binary_string, 2)
    return decimal_number

wire_dict = phrase_wire()
wire_dict = gate_connection(wire_dict)
new_number = form_new_number(wire_dict)
print(new_number)
