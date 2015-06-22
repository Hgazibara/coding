class Plugboard(object):
    def __init__(self, wires=None):
        """
        wires: This is the mapping of pairs of characters
        """
        self.wires = {}

        if wires:
            assert len(wires) % 2 == 0
            assert len(wires) <= 20
            assert len(wires) == len(set(wires))

            for x, y in zip(wires[0::2], wires[1::2]):
                self.wires[x], self.wires[y] = y, x
                
    def process(self, c):
        """
        c: The single character to process
        """
        return self.wires.get(c, c)
