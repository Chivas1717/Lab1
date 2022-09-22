
import argparse

def optimal_weight(W, w):

    bars = [0] + w
    print(bars)
    gold_dict = {}
    for i in range(0, W+1):
        gold_dict[(i, bars[0])] = 0
    for i in bars:
        gold_dict[(0, i)] = 0
    # print(gold_dict)
    for i in range(1, len(bars)):
        for weight in range(1, W+1):
            gold_dict[(weight, bars[i])] = gold_dict[(weight, bars[i-1])]
            if bars[i] <= weight:
                val = gold_dict[(weight-bars[i], bars[i-1])] + bars[i]
                if gold_dict[(weight, bars[i])] < val:
                    gold_dict[(weight, bars[i])] = val
    # print(gold_dict)
    return max(gold_dict.values())



parser = argparse.ArgumentParser()
parser.add_argument("-g", type=int)
parser.add_argument("-w", nargs='+', type=int)
args = parser.parse_args()
print(optimal_weight(args.g, args.w))