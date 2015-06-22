def hamming(n):
    hamming_numbers = iter(HammingGenerator())

    for _ in xrange(n - 1):
        next(hamming_numbers)

    return next(hamming_numbers)


class HammingGenerator(object):

    def __init__(self):
        self.containers = [[], [], []]
        self.state = 1

    def __iter__(self):
        while True:
            num = self.state
            yield num

            for container, x in zip(self.containers, [2, 3, 5]):
                container.append(num * x)

            next_num = min([container[0] for container in self.containers])

            for container in self.containers:
                if next_num in container:
                    container.remove(next_num)

            self.state = next_num
