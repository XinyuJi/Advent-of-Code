def count_path(data):
    graph = {}
    for line in data:
        if ":" not in line:
            continue
        left, right = line.split(":", 1)
        graph[left.strip()] = right.strip().split()

    memo = {}
    def dfs(node, seen_dac, seen_fft):
        key = (node, seen_dac, seen_fft)
        if key in memo:
            return memo[key]

        if node == "dac":
            seen_dac = True
        elif node == "fft":
            seen_fft = True

        if node == "out":
            return 1 if (seen_dac and seen_fft) else 0

        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt, seen_dac, seen_fft)

        memo[key] = total
        return total
    return dfs("svr", False, False)

if __name__ == "__main__":
    with open("11.txt") as f:
        data = f.read().splitlines()
    result = count_path(data)
    print("Result:", result)
