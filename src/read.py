import json

from Model import Model


def read():
    file = open("../res/hmm_simple.json")
    data = json.load(file)

    states = data["states"]
    initial_distribution = data["initial_distribution"]
    transition_probabilities = data["transition_probabilities"]
    alphabet = data["alphabet"]
    output_probabilities = data["output_probabilities"]

    model = Model(states, initial_distribution, transition_probabilities, alphabet, output_probabilities)

    file = open("../res/hmm_observation.json")
    data = json.load(file)

    observations = []
    for date in data:
        observations.append(Model.Observation(model.alphabet.index(date), date))

    file.close()

    return model, observations
