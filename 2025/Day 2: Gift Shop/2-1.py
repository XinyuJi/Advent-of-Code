def sum_invalid_ids(data):
    data_ranges = [
        tuple(map(int, part.split('-')))
        for part in data.split(',') if part.strip()
    ]

    max_upper = max(b for _, b in data_ranges)
    max_len = len(str(max_upper))
    invalid_ids = []

    for k in range(1, max_len // 2 + 1):
        mult = 10 ** k + 1
        start_s = 10 ** (k - 1)
        end_s = 10 ** k - 1

        for s in range(start_s, end_s + 1):
            n = s * mult   # n = s*(10^k + 1)
            if n > max_upper:
                break
            for a, b in data_ranges:
                if a <= n <= b:
                    invalid_ids.append(n)
                    break

    total = sum(invalid_ids)
    return total, invalid_ids

if __name__ == "__main__":
    with open("2.txt", "r") as f:
        data = f.read().strip()
    total, nums = sum_invalid_ids(data)
    print("Found invalid IDs:", nums)
    print("Sum:", total)
