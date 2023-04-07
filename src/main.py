from Decode import Decode
from Evaluate import Eval
from read import read

if __name__ == '__main__':
    model, observations = read()
    evaluation = Eval(model, observations)
    decode = Decode(model, observations)
    prob = evaluation.forward(len(observations), 0)
    maximum, states = decode.forward(len(observations), 0)
    rel_maximum = maximum / prob
    print("Probability:", prob)
    print("Best States:")
    for state in states:
        print("  ", state.name)
    print("absolute Maximum Probability:", maximum)
    print("relative Maximum Probability:", rel_maximum)
