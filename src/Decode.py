class Decode:
    def __init__(self, model, observations):
        self.observations = observations
        self.model = model

    def viterbi(self, time, state):
        if time == 0:
            return self.model.initial_distribution[state.index] * self.model.output_probabilities[state.name][
                self.observations[time].index], [state]
        elif time < len(self.observations):
            maximum = 0
            states = []
            best_state = 0
            for i in self.model.states:
                value, states = self.viterbi(time - 1, i)
                value *= self.model.transition_probabilities[i.name][state.index]
                if value > maximum:
                    maximum = value
                    best_state = i
            states.append(best_state)
            return maximum * self.model.output_probabilities[state.name][self.observations[time].index], states
        else:
            maximum = 0
            states = []
            best_state = 0
            for i in self.model.states:
                value, states = self.viterbi(time - 1, i)
                if value > maximum:
                    maximum = value
                    best_state = i
            states.append(best_state)
            return maximum, states
