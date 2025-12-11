def count_path(data):
    graph = {}
    for line in data:
        left, right = line.split(":")
        graph[left.strip()] = right.strip().split()

    results = []
    path = []

    def dfs(node):
        path.append(node)
        if node == "out":
            results.append(path.copy())
        else:
            for nxt in graph.get(node, []):
                dfs(nxt)
        path.pop()

    dfs("you")
    return len(results)

if __name__ == "__main__":
    with open("11.txt") as f:
        data = f.read().splitlines()
    result = count_path(data)
    print("Result:", result)
