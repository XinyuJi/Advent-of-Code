def max_12_digits(line):
    k = 12
    n = len(line)
    result = []
    start = 0

    for picks in range(k, 0, -1):
        end = n - picks
        best_digit = '-1'
        best_pos = start
        for pos in range(start, end + 1):
            if line[pos] > best_digit:
                best_digit = line[pos]
                best_pos = pos
                if best_digit == '9':
                    break

        result.append(best_digit)
        start = best_pos + 1
    return int("".join(result))

def total_output(data):
    total = 0
    max_nums = []
    for line in data.splitlines():
        line = line.strip()
        total += max_12_digits(line)
        max_nums.append(max_12_digits(line))
    return total, max_nums

if __name__ == "__main__":
    with open("3.txt", "r") as f:
        data = f.read()
    total, nums = total_output(data)
    print("Values:", nums)
    print("Sum:", total)
