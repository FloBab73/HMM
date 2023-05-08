class Evaluate:
    def __init__(self, model, observations):
        self.observations = observations
        self.model = model

    def forward(self, time, state=None):
        if time == 0:  # Initialization
            return self.model.initial_distribution[state.index] * self.model.output_probabilities[state.name][
                self.observations[time].index]
        elif time < len(self.observations):  # Recursion
            sigma = 0
            for i in self.model.states:
                sigma += self.forward(time - 1, i) * \
                         self.model.transition_probabilities[i.name][state.index]
            return sigma * self.model.output_probabilities[state.name][self.observations[time].index]
        else:  # Termination
            sigma = 0
            for i in self.model.states:
                sigma += self.forward(time - 1, i)
            return sigma
