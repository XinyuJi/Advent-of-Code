def count_fresh_ids(data):
    lines = [line for line in data]
    line_index = lines.index("")

    range_lines = lines[:line_index]
    ranges = []
    for r in range_lines:
        start, end = map(int, r.split("-"))
        ranges.append((start, end))

    ranges.sort()
    merged = []
    for s, e in ranges:
        if not merged or s > merged[-1][1] + 1:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    total = 0
    for s, e in merged:
        total += (e - s + 1)
    return total

if __name__ == "__main__":
    with open("5.txt", "r") as f:
        data = f.read().strip().splitlines()
    total = count_fresh_ids(data)
    print("Total fresh ids:", total)
