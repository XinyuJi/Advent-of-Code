def count_regions(lines):
    result = 0
    shapes = []
    shape_cell_counts = []
    shape_buffer = []

    state = 0
    for raw_line in lines:
        line = raw_line.strip()
        if state == 0:
            if line.endswith(":"):
                state = 1
                continue

            parts = line.split()
            counts = list(map(int, parts[1:]))

            dim = parts[0][:-1]
            width, height = map(int, dim.split("x"))

            if sum(counts) <= (width // 3) * (height // 3):
                result += 1
            else:
                required = 0
                for i, c in enumerate(counts):
                    required += shape_cell_counts[i] * c
                assert required > width * height

        else:
            shape_buffer.append(line)

            if state == 3:
                cell_count = sum(row.count("#") for row in shape_buffer)
                shapes.append(shape_buffer)
                shape_cell_counts.append(cell_count)

                shape_buffer = []
                state = 0
            else:
                state += 1
    return result

if __name__ == "__main__":
    with open("12.txt") as f:
        data = f.read().splitlines()
    result = count_regions(data)
    print("Result:", result)
