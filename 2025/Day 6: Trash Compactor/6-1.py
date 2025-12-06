def do_math_homework(data):
    lines = [line.rstrip("\n") for line in data]
    height = len(lines)
    width = max(len(line) for line in lines)
    lines = [line.ljust(width) for line in lines]

    empty_cols = []
    for c in range(width):
        if all(lines[r][c] == " " for r in range(height)):
            empty_cols.append(c)

    segments = []
    start = 0
    for c in empty_cols + [width]:
        if c > start:
            segments.append((start, c))
        start = c + 1

    total_sum = 0
    for (left, right) in segments:
        block = [line[left:right] for line in lines]

        op_line = block[-1].strip()
        if op_line == "+":
            op = "+"
        elif op_line == "*":
            op = "*"
        else:
            continue

        nums = []
        for row in block[:-1]:
            s = row.strip()
            if s:
                nums.append(int(s))

        if not nums:
            continue

        if op == "+":
            result = sum(nums)
        else:  # op == "*"
            result = 1
            for n in nums:
                result *= n

        total_sum += result
    return total_sum

if __name__ == "__main__":
    with open("6.txt", "r") as f:
        data = f.read().strip().splitlines()
    total = do_math_homework(data)
    print("Sum:", total)
