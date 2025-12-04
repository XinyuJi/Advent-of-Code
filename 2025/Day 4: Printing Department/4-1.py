def count_accessible_rolls(data):
    grid = [list(line) for line in data]
    h, w = len(grid), len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    accessible_rolls = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] != '@':
                continue

            neighbour_rolls = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '@':
                    neighbour_rolls += 1

            if neighbour_rolls < 4:
                accessible_rolls += 1
    return accessible_rolls

if __name__ == "__main__":
    with open("4.txt", "r") as f:
        data = f.read().strip().splitlines()
    total = count_accessible_rolls(data)
    print("Accessible rolls:", total)
