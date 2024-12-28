with open('24.txt', 'r') as file:
    wire, operations = file.read().split('\n\n')

def phrase_wire_and_operations():
    wire_dict = {}
    for line in wire.strip().splitlines():
        key, value = line.split(':')
        wire_dict[key.strip()] = int(value.strip())

    operations_list = []
    highest_z = "z0"
    for line in operations.strip().splitlines():
        operand1, operator, operand2, _, result = line.split(" ")
        operations_list.append((operand1, operator, operand2, result))
        if result.startswith("z") and int(result[1:]) > int(highest_z[1:]):
            highest_z = result
    return wire_dict, operations_list, highest_z

def perform_operation(operator, operand1, operand2):
    if operator == "AND":
        return operand1 & operand2
    elif operator == "OR":
        return operand1 | operand2
    elif operator == "XOR":
        return operand1 ^ operand2

def find_wrong_connections(wire_dict, operations_list, highest_z):
    wrong_connections = set()
    operand_prefixes = {'x', 'y', 'z'}
    for operand1, operator, operand2, result in operations_list:
        if result.startswith("z") and operator != "XOR" and result != highest_z:
            wrong_connections.add(result)
        if operator == "XOR" and all(operand[0] not in operand_prefixes for operand in [operand1, operand2, result]):
            wrong_connections.add(result)
        if operator == "AND" and "x00" not in [operand1, operand2]:
            for sub_operand1, sub_operator, sub_operand2, sub_result in operations_list:
                if (result == sub_operand1 or result == sub_operand2) and sub_operator != "OR":
                    wrong_connections.add(result)
        if operator == "XOR":
            for sub_operand1, sub_operator, sub_operand2, sub_result in operations_list:
                if (result == sub_operand1 or result == sub_operand2) and sub_operator == "OR":
                    wrong_connections.add(result)
    return ",".join(sorted(wrong_connections))

wire_dict, operations_list, highest_z = phrase_wire_and_operations()
wrong_connections = find_wrong_connections(wire_dict, operations_list, highest_z)
print(wrong_connections)
