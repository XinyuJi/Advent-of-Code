def max_bank_value(line):
    max_val = 0
    for i in range(len(line)-1):
        di = ord(line[i]) - 48
        for j in range(i+1, len(line)):
            dj = ord(line[j]) - 48
            val = di*10 + dj
            if val > max_val:
                max_val = val
                if max_val == 99:
                    return 99
    return max_val

def total_output(data):
    total = 0
    for line in data.splitlines():
        line = line.strip()
        total += max_bank_value(line)
    return total

if __name__ == "__main__":
    with open("3.txt", "r") as f:
        data = f.read()
    total = total_output(data)
    print("Sum:", total)
