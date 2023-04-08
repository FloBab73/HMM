from Decode import Decode
from Evaluate import Eval
from read import read

if __name__ == '__main__':
    model, observations = read()
    evaluation = Eval(model, observations)
    decode = Decode(model, observations)

    prob = evaluation.forward(len(observations), 0)
    print("probability: " + "{0:.5f}".format(prob))
    if prob != 0:
        maximum, states = decode.viterbi(len(observations), 0)
        rel_maximum = maximum / prob
        print("best states:")
        for state in states:
            print("  ", state.name)
        print("absolute maximum probability: " + "{0:.5f}".format(maximum))
        print("relative maximum probability: " + "{0:.5f}".format(rel_maximum))
    else:
        print("No possible path")
