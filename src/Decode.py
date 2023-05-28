import numpy as np


class Decode:
    def __init__(self, model, observations):
        self.observations = observations
        self.model = model
        self.probs = np.zeros((len(observations), len(model.states)))
        self.best_states = np.empty((len(observations), len(model.states)), dtype=object)

    def viterbi_recursive(self, time, state):
        if time == 0:  # Initialization
            return self.model.initial_distribution[state.index] * self.model.output_probabilities[state.name][
                self.observations[time].index], []
        elif time < len(self.observations):  # Recursion
            maximum = 0
            states = []
            best_state = None
            for i in self.model.states:
                value, states = self.viterbi_recursive(time - 1, i)
                value = value * self.model.transition_probabilities[i.name][state.index]
                if value > maximum:
                    maximum = value
                    best_state = i
            states.append(best_state)
            return maximum * self.model.output_probabilities[state.name][self.observations[time].index], states
        else:  # Termination
            maximum = 0
            states = []
            best_state = None
            for i in self.model.states:
                value, states = self.viterbi_recursive(time - 1, i)
                if value > maximum:
                    maximum = value
                    best_state = i
            states.append(best_state)
            return maximum, states

    def viterbi(self):
        # Initialization
        for state in self.model.states:
            self.probs[0][state.index] = self.model.initial_distribution[state.index] * \
                                         self.model.output_probabilities[state.name][self.observations[0].index]

        # Recursion
        for observation in self.observations[1:]:
            for current_state in self.model.states:
                maximum_value = 0
                best_state = None
                for prev_state in self.model.states:
                    value = self.probs[observation.time - 1][prev_state.index] * \
                            self.model.transition_probabilities[prev_state.name][current_state.index]
                    if value > maximum_value:
                        maximum_value = value
                        best_state = prev_state
                self.best_states[observation.time][current_state.index] = best_state

                self.probs[observation.time][current_state.index] = maximum_value * self.model.output_probabilities[
                    current_state.name][observation.index]

        # Termination
        maximum_value = 0
        best_state = None
        for state in self.model.states:
            value = self.probs[len(self.observations)-1][state.index]
            if value > maximum_value:
                maximum_value = value
                best_state = state
        final_states = [best_state]
        counter = 0
        for observation in reversed(self.observations[1:]):
            final_states.append(self.best_states[observation.time][final_states[counter].index])
            counter += 1
        return maximum_value, final_states
