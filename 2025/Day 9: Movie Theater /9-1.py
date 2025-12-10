def largest_area_of_rectangle(data):
    max_area = 0
    for i, (x1, y1) in enumerate(data):
        for x2, y2 in data[:i]:
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            rect_area = width * height
            if rect_area > max_area:
                max_area = rect_area
    return max_area

if __name__ == "__main__":
    with open("9.txt") as f:
        data = [tuple(map(int, line.split(','))) for line in f]
    result = largest_area_of_rectangle(data)
    print("Result:", result)
