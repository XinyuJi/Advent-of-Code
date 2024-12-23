from collections import defaultdict

with open('23.txt', 'r') as file:
    network_map = [tuple(line.strip().split('-')) for line in file]

def build_connection_graph(network_map):
    graph = defaultdict(list)
    for comp_a, comp_b in network_map:
        graph[comp_a].append(comp_b)
        graph[comp_b].append(comp_a)
    return graph

def bron_kerbosch(current_clique, potential_nodes, excluded_nodes):
    if not potential_nodes and not excluded_nodes:
        return [current_clique]
    cliques = []
    for node in list(potential_nodes):
        new_clique = current_clique | {node}
        new_potential_nodes = potential_nodes & set(graph[node])
        new_excluded_nodes = excluded_nodes & set(graph[node])
        cliques += bron_kerbosch(new_clique, new_potential_nodes, new_excluded_nodes)
        potential_nodes.remove(node)
        excluded_nodes.add(node)
    return cliques

def find_largest_clique(graph):
    potential_nodes = set(graph.keys())
    current_clique = set()
    excluded_nodes = set()
    cliques = bron_kerbosch(current_clique, potential_nodes, excluded_nodes)
    largest_clique = max(cliques, key=len) if cliques else []
    return sorted(largest_clique)

graph = build_connection_graph(network_map)
largest_clique = find_largest_clique(graph)
result = ",".join(largest_clique)
print(result)
