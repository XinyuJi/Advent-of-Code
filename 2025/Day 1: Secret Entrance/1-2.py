with open('1.txt', 'r') as file:
    data = file.read().strip().splitlines()

def count_zero(rotations):
    pos = 50
    zero_count = 0

    for r in rotations:
        direction = r[0]
        distance = int(r[1:])

        if direction == "L":
            for _ in range(distance):
                pos = (pos - 1) % 100
                if pos == 0:
                    zero_count += 1
        else:
            zero_count += (pos + distance) // 100
            pos = (pos + distance) % 100

    return zero_count

password = count_zero(data)
print(password)
