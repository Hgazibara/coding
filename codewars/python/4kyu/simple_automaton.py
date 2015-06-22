class Automaton(object):

    transitions = {
        ('q1', '1'): 'q2',
        ('q1', '0'): 'q1',
        ('q2', '0'): 'q3',
        ('q2', '1'): 'q2',
        ('q3', '0'): 'q2',
        ('q3', '1'): 'q2',
    }

    def __init__(self):
        self.state = 'q1'

    def read_commands(self, commands):
        for command in commands:
            self.state = self.transitions[(self.state, command)]

        return self.state == 'q2'


my_automaton = Automaton()
