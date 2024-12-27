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

def count_step_differences(distances):
    count = 0
    for current, current_distance in list(distances.items())[::-1]:
        for direction in directions:
            neighbor = (current[0] + 2 * direction[0], current[1] + 2 * direction[1])
            if neighbor in distances:
                neighbor_distance = distances[neighbor]
                if current_distance - neighbor_distance - 2 >= 100:
                    count += 1
    return count

start, end = find_start_and_end(map)
distances = calculate_distances(start, end, map)
result = count_step_differences(distances)
print(result)
