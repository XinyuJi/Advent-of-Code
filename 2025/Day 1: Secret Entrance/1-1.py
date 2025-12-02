def count_zero(rotations):
    pos = 50
    zero_count = 0

    for r in rotations:
        direction = r[0]
        distance = int(r[1:])

        if direction == "L":
            pos = (pos - distance) % 100
        else:
            pos = (pos + distance) % 100

        if pos == 0:
            zero_count += 1

    return zero_count

if __name__ == "__main__":
    with open('1.txt', 'r') as file:
        data = file.read().strip().splitlines()
    password = count_zero(data)
    print(password)
