from bisect import bisect_right

def parse_data_ranges(ranges_str):
    parts = [p.strip() for p in ranges_str.split(",") if p.strip()]
    intervals = [tuple(map(int, p.split("-"))) for p in parts]
    intervals.sort()

    merged = []
    for a, b in intervals:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            if b > merged[-1][1]:
                merged[-1][1] = b
    return [(x, y) for x, y in merged]

def in_any_interval(n, intervals, starts):
    idx = bisect_right(starts, n)
    if idx == 0:
        return False
    a, b = intervals[idx - 1]
    return a <= n <= b

def sum_invalid_ids(ranges_str):
    data_ranges = parse_data_ranges(ranges_str)
    starts = [a for a, _ in data_ranges]
    max_upper = data_ranges[-1][1]
    max_len = len(str(max_upper))

    invalid_ids = set()

    for k in range(1, max_len):
        pow10k = 10 ** k
        start_s = 10 ** (k - 1)
        end_s = 10 ** k - 1

        m_max = max_len // k
        if m_max < 2:
            continue

        for m in range(2, m_max + 1):
            pow_km = 10 ** (k * m)
            rep = (pow_km - 1) // (pow10k - 1)

            s_max_upper = max_upper // rep
            s_max = min(end_s, s_max_upper)
            if start_s > s_max:
                continue

            for s in range(start_s, s_max + 1):
                n = s * rep
                if in_any_interval(n, data_ranges, starts):
                    invalid_ids.add(n)

    invalid_ids = sorted(invalid_ids)
    total = sum(invalid_ids)
    return total, invalid_ids

if __name__ == "__main__":
    with open("2.txt", "r") as f:
        data = f.read().strip()
    total, nums = sum_invalid_ids(data)
    print("Found invalid IDs:", nums)
    print("Sum:", total)
