with open('11.txt', 'r') as file:
    data = file.read()
input=data.split()

def stone_blink(input):
    new_list = []
    for num in input:
        num_int = int(num)
        if num_int == 0:
            new_list.append('1')
        else:
            num_len = len(num)
            if num_len%2 == 0:
                mid = num_len // 2
                left_p = num[:mid]
                right_p = int(num[mid:])
                new_list.append(left_p)
                new_list.append('0' if right_p == 0 else str(right_p))
            else:
                new_list.append(str(num_int * 2024))
    return new_list

def process_iterations(input, times):
    for _ in range(times):
        input = stone_blink(input)
    return input

result = process_iterations(input, 25)
print(len(result))
