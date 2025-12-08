from itertools import combinations

def dist(pair):
    a, b = pair
    return sum((x - y) ** 2 for x, y in zip(a, b))

def find(x, parent):
    while parent[x] is not None:
        x = parent[x]
    return x

def multiply_three(points):
    pairs = sorted(combinations(points, 2), key=dist)
    parent = {p: None for p in points}
    cnt = 0
    for i, (a, b) in enumerate(pairs):
        ra, rb = find(a, parent), find(b, parent)
        if ra != rb:
            parent[ra] = rb
            cnt += 1
            if cnt == len(points) - 1:
                result = a[0] * b[0]
    return result

if __name__ == "__main__":
    with open("8.txt") as f:
        pts = [tuple(map(int, line.strip().split(","))) for line in f]
    print("Result:", multiply_three(pts))
