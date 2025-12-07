from collections import defaultdict

def count_timelines(grid):
    height = len(grid)
    weight = len(grid[0]) if height else 0
    
    sr = sc = None
    for r in range(height):
        for c in range(weight):
            if grid[r][c] == 'S':
                sr, sc = r, c
                break
        if sr is not None:
            break

    beams = {sc: 1}
    for r in range(sr + 1, height):
        current = dict(beams)
        while True:
            updated = defaultdict(int)
            for c, cnt in current.items():
                if 0 <= c < weight and grid[r][c] == '^':
                    if c - 1 >= 0:
                        updated[c - 1] += cnt
                    if c + 1 < weight:
                        updated[c + 1] += cnt
                else:
                    updated[c] += cnt
            updated = dict(updated)
            if updated == current:
                break
            current = updated

        beams = {c: cnt for c, cnt in current.items() if grid[r][c] != '^'}
        if not beams:
            return 0
    return sum(beams.values())

if __name__ == "__main__":
    with open("7.txt") as f:
        data = f.read().splitlines()
        grid = [list(row) for row in data]
    print("Sum:", count_timelines(grid))
