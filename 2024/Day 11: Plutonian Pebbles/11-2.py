from collections import defaultdict

with open('11.txt', 'r') as file:
    data = file.read()
input=data.split()

def stone_blink(input, times):
    input_dict = defaultdict(int)
    for num in input:
        input_dict[int(num)] += 1

    for _ in range(times):
        update_dict = defaultdict(int)
        for k, v in input_dict.items():
            update_dict[k] -= v
            num_str = str(k)
            num_len = len(num_str)
            if k == 0:
                update_dict[1] += v
            elif num_len % 2 == 0:
                mid = num_len // 2
                l, r = int(num_str[:mid]), int(num_str[mid:])
                update_dict[l] += v
                update_dict[r] += v
            else:
                update_dict[k*2024] += v
    
        for k, v in update_dict.items():
            input_dict[k] += v
            if input_dict[k] ==0:
                input_dict.pop(k)
    return input_dict

result = stone_blink(input, 75)
print(sum(result.values()))
