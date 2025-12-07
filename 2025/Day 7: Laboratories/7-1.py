def count_the_beam_splits(grid):
    height = len(grid)
    weight = len(grid[0])

    sr = sc = None
    for r in range(height):
        for c in range(weight):
            if grid[r][c] == "S":
                sr, sc = r, c
                break
        else:
            continue
        break

    splits = 0
    beams = {sc}
    for r in range(sr + 1, height):
        current = set(beams)
        while True:
            changed = False
            new_set = set()
            for c in current:
                if grid[r][c] == "^":
                    splits += 1
                    changed = True
                    if c > 0:
                        new_set.add(c - 1)
                    if c < weight - 1:
                        new_set.add(c + 1)
                else:
                    new_set.add(c)

            if new_set == current:
                break
            current = new_set

        beams = {c for c in current if grid[r][c] != "^"}
        if not beams:
            break
    return splits

if __name__ == "__main__":
    with open("7.txt") as f:
        data = f.read().splitlines()
        grid = [list(row) for row in data]
    print("Sum:", count_the_beam_splits(grid))
