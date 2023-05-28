import numpy as np


class Evaluate:
    def __init__(self, model, observations):
        self.observations = observations
        self.model = model
        self.probs = np.zeros((len(observations), len(model.states)))

    def forward_recursive(self, time, state=None):
        if time == 0:  # Initialization
            return self.model.initial_distribution[state.index] * self.model.output_probabilities[state.name][
                self.observations[time].index]
        elif time < len(self.observations):  # Recursion
            sigma = 0
            for i in self.model.states:
                sigma += self.forward_recursive(time - 1, i) * \
                         self.model.transition_probabilities[i.name][state.index]
            return sigma * self.model.output_probabilities[state.name][self.observations[time].index]
        else:  # Termination
            sigma = 0
            for i in self.model.states:
                sigma += self.forward_recursive(time - 1, i)
            return sigma

    def forward(self):
        # Initialization
        for state in self.model.states:
            self.probs[0][state.index] = self.model.initial_distribution[state.index] * \
                                         self.model.output_probabilities[state.name][self.observations[0].index]

        # Recursion
        for observation in self.observations[1:]:
            for current_state in self.model.states:
                sigma = sum(self.probs[observation.time - 1][prev_state.index] *
                            self.model.transition_probabilities[prev_state.name][current_state.index] for prev_state in
                            self.model.states)
                self.probs[observation.time][current_state.index] = sigma * self.model.output_probabilities[
                    current_state.name][observation.index]

        # Termination
        return sum(self.probs[len(self.observations) - 1][state.index] for state in self.model.states)
