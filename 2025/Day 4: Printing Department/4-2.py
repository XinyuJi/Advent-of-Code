def count_removed_rolls(data):
    grid = [list(line) for line in data]
    h, w = len(grid), len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    removed_rolls = 0
    while True:
        to_remove = []
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
                    to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        removed_rolls += len(to_remove)
    return removed_rolls

if __name__ == "__main__":
    with open("4.txt", "r") as f:
        data = f.read().strip().splitlines()
    total = count_removed_rolls(data)
    print("Removed rolls:", total)
