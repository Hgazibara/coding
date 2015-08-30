import collections

class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        if node is None:
            return node

        self.clones = {}

        queue = collections.deque()
        queue.append(node)

        new_node = UndirectedGraphNode(node.label)
        self.clones[node] = new_node

        while queue:
            top = queue.popleft()

            for other in top.neighbors:
                other_copy = self.clones.get(other, None) or UndirectedGraphNode(other.label)
                self.clones[top].neighbors.append(other_copy)

                if not other in self.clones:
                    self.clones[other] = other_copy
                    queue.append(other)

        return new_node
