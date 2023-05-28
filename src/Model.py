class Model:
    class State:
        def __init__(self, index, name):
            self.name = name
            self.index = index

    class Observation:
        def __init__(self, index, name, time):
            self.name = name
            self.index = index
            self.time = time

    def __init__(self, states, initial_distribution, transition_probabilities, alphabet, output_probabilities):
        self.output_probabilities = output_probabilities
        self.alphabet = alphabet
        self.transition_probabilities = transition_probabilities
        self.initial_distribution = initial_distribution
        self.states = []
        for idx, state in enumerate(states):
            self.states.append(self.State(idx, state))
