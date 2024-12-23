from collections import defaultdict

with open('23.txt', 'r') as file:
    network_map = [tuple(line.strip().split('-')) for line in file]

def build_connection_graph(network_map):
    graph = defaultdict(list)
    for comp_a, comp_b in network_map:
        graph[comp_a].append(comp_b)
        graph[comp_b].append(comp_a)
    return graph

def find_triplets(graph):
    triplets = set()
    for start in graph:
        for mid in graph[start]:
            for end in graph[mid]:
                if end != start and start in graph[end]: 
                    triplet = tuple(sorted([start, mid, end]))
                    triplets.add(triplet)
    return triplets

def find_computer_starts_with_t(triplets):
    result = set()
    for triplet in triplets:
        for computer in triplet:
            if computer.startswith('t'):
                result.add(triplet)
    return len(result)

graph = build_connection_graph(network_map)
triplets = find_triplets(graph)
result = find_computer_starts_with_t(triplets)
print(result)
