import collections

Node = collections.namedtuple('Node', 'word, level')

class Solution(object):
    def ladderLength(self, begin_word, end_word, word_dict):
        word_dict.add(end_word)

        start_queue = Queue(begin_word)
        end_queue = Queue(end_word)

        while start_queue and end_queue:
            if len(start_queue) < len(end_queue):
                output = self.process(start_queue, end_queue, word_dict)
                if output:
                    return output
            else:
                output = self.process(end_queue, start_queue, word_dict)
                if output:
                    return output

        return 0

    def process(self, start_queue, end_queue, word_dict):
        while start_queue and start_queue[0].level == start_queue.level:
            neighbours = self.findNeighbours(start_queue[0].word, word_dict)

            for word in neighbours:
                if not start_queue.has_visited(word):
                    start_queue.visit(word)
                    if end_queue.has_visited(word):
                        return start_queue[0].level + end_queue[0].level
                    start_queue.append(Node(word, start_queue.level + 1))

            start_queue.pop()
        start_queue.level += 1

    def findNeighbours(self, word, word_dict):
        for i, char in enumerate(word):
            s = list(word)
            for j in xrange(97, 123):
                s[i] = chr(j)
                new_word = ''.join(s)
                if new_word in word_dict and self.areNeighbours(word, new_word):
                    yield new_word

    def areNeighbours(self, word, other):
        changes = 0
        for c1, c2 in zip(word, other):
            if c1 != c2:
                changes += 1
            if changes > 1:
                return False
        return changes == 1


class Queue(object):
    def __init__(self, init=None):
        self.queue = collections.deque()
        self.level = 1
        self.visited = set()

        if init:
            self.queue.append(Node(init, self.level))
            self.visited.add(init)

    def __len__(self):
        return len(self.queue)

    def __getitem__(self, key):
        return self.queue[key]

    def visit(self, word):
        self.visited.add(word)

    def has_visited(self, word):
        return word in self.visited

    def append(self, node):
        self.queue.append(node)

    def pop(self):
        self.queue.popleft()
