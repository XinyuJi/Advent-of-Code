def count_fresh_ids(data):
    lines = [line for line in data]
    line_index = lines.index("")

    range_lines = lines[:line_index]
    id_lines = lines[line_index+1:]

    ranges = []
    for r in range_lines:
        start, end = map(int, r.split("-"))
        ranges.append((start, end))

    ranges.sort()
    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    def is_fresh(x):
        for s, e in merged:
            if s <= x <= e:
                return True
        return False

    available_ids = [int(x) for x in id_lines]
    return sum(is_fresh(x) for x in available_ids)

if __name__ == "__main__":
    with open("5.txt", "r") as f:
        data = f.read().strip().splitlines()
    total = count_fresh_ids(data)
    print("Total fresh ids:", total)
