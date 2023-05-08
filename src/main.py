from Decode import Decode
from Evaluate import Evaluate
from read import read

if __name__ == '__main__':
    model, observations = read()
    evaluation = Evaluate(model, observations)
    decode = Decode(model, observations)

    prob = evaluation.forward(len(observations))
    print("forward probability: " + "{0:.5f}".format(prob))
    if prob != 0:
        maximum, states = decode.viterbi(len(observations), 0)
        rel_maximum = maximum / prob
        print("viterbi states:")
        for state in states:
            print("  ", state.name)
        print("absolute path probability: " + "{0:.5f}".format(maximum))
        print("relative path probability: " + "{0:.5f}".format(rel_maximum))
    else:
        print("No possible path")
