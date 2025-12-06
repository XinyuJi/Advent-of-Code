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

    total = 0
    for left, right in segments:
        block = [line[left:right] for line in lines]
        op = block[-1].strip()
        if op not in {"+", "*"}:
            continue

        numbers = []
        for c in range(right - left - 1, -1, -1):
            col_digits = [block[r][c] for r in range(height - 1)]
            col_digits = "".join(d for d in col_digits if d.isdigit())
            if col_digits:
                numbers.append(int(col_digits))

        if not numbers:
            continue

        if op == "+":
            total += sum(numbers)
        else:
            p = 1
            for n in numbers:
                p *= n
            total += p
    return total

if __name__ == "__main__":
    with open("6.txt") as f:
        data = f.read().splitlines()
    print("Sum:", do_math_homework(data))
