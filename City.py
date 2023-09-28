class City:

    def __init__(self, name, state, pop):
        self.name = name
        self.state = state
        self.pop = pop

    def __str__(self):
        return '{}, {} (pop: {})'.format(self.name, self.state, self.pop)
