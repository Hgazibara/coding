def loop_size(node):
    visited = set()
    chain = []

    while not node.__str__() in visited:
        visited.add(node.__str__())
        chain.append(node.__str__())
        node = node.next

    return len(chain) - chain.index(node.__str__())
