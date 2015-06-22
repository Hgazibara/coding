from collections import defaultdict, deque

def recoverSecret(triplets):
    connections = make_connections(triplets)
    sorted_letters = sort(connections)

    return ''.join(sorted_letters)


def make_connections(triplets):
    connections = defaultdict(list)

    for triplet in triplets:
        for a, b in zip(triplet[:-1], triplet[1:]):
            connections[a].append(b)

    return connections


def sort(connections):
    sorted_letters = deque()
    nodes = set(connections.keys() + sum(connections.values(), []))

    marked_nodes = set()

    def visit(node):
        if not node in marked_nodes:
            for next_node in connections[node]:
                visit(next_node)
            marked_nodes.add(node)
            sorted_letters.appendleft(node)

    for node in nodes:
        if not node in marked_nodes:
            visit(node)

    return sorted_letters
