with open('20.txt', 'r') as file:
    map = file.read().splitlines()

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_start_and_end(map):
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
            elif cell == "E":
                end = (i, j)
    return start, end

def is_valid(x, y, map):
    return 0 <= x < len(map) and 0 <= y < len(map[x]) and map[x][y] != '#'

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calculate_distances(start, end, map):
    distances = {}
    current = end
    previous = end
    step_count = 0

    while current != start:
        distances[current] = step_count
        step_count += 1
        for direction in directions:
            next_position = (current[0] + direction[0], current[1] + direction[1])
            if next_position != previous and is_valid(*next_position, map):
                previous = current
                current = next_position
                break
    distances[start] = step_count
    return distances

def count_pairs_with_differences(distances):
    count = 0
    for point1, distance1 in reversed(list(distances.items())):
        for point2, distance2 in distances.items():
            manhattan_dist = manhattan_distance(point1, point2)
            if manhattan_dist <= 20 and distance2 - distance1 - manhattan_dist >= 100:
                count += 1
    return count

start, end = find_start_and_end(map)
distances = calculate_distances(start, end, map)
result = count_pairs_with_differences(distances)
print(result)
