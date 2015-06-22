class Plugboard(object):
    def __init__(self, wires=None):
        """
        wires: This is the mapping of pairs of characters
        """
        self.wires = {}

        if not wires:
            return

        if len(wires) > 20:
            raise ValueError('Too many wires defined')

        for wire in [wires[i:i+2] for i in range(0, len(wires), 2)]:
            if wire[0] in self.wires or wire[1] in self.wires:
                raise ValueError('Too many wires defined')

            self.wires[wire[0]] = wire[1]
            self.wires[wire[1]] = wire[0]
                
    def process(self, c):
        """
        c: The single character to process
        """
        return self.wires[c] if c in self.wires else c
