"Analyzes how similar neighbors in NC are to each other"

__author__ = "Jay Patel"

"Reads in file containing which nodes are connected to" \
"each other and the distances between them and organizes " \
"data into a dictionary. Also reads a given voting results file" \
"into a list "

import matplotlib.pyplot as plt
import numpy as np

def readEdgesFile(filename):
    d = {}
    f = open(filename)
    for line in f:
        split = line.split()
        node1 = int(split[0])
        node2 = int(split[1])
        dist = int(split[2])
        if node1 not in d:
            tupList = [(node2, dist)]
            d[node1] = tupList
        else:
            d[node1].append((node2, dist))
    return d

def readVotingFile(filename):
    repVoting = [0 for i in range(2693)]
    f = open(filename)
    for line in f:
        split = line.split()
        node = int(split[0])
        dem = int(split[2])
        rep = int(split[3])
        ind = int(split[4])
        total = dem + rep + ind
        if total == 0:
            continue
        repPerc = rep / total
        repVoting[node] = repPerc
    return repVoting

def makeOneNodePlot(d, repVoting, node):
    # JUST TRY ONE NODE GRAPH FOR NOW

    tuples = d[node]
    tuples.append((node, 0))
    data = [(tup[1], repVoting[tup[0]]) for tup in tuples]
    data = sorted(data, key=lambda t: (t[0]))
    dist = [t[0] for t in data]
    votes = [t[1] for t in data]
    plt.plot(dist, votes, color="red")
    plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

def makeAveragePlot(d, repVoting):

    return ""

if __name__ == '__main__':
    d = readEdgesFile("../data/NC_Edges_Lengths.txt")
    repVoting = readVotingFile("../data/VTDLevel_USHOUSEOFREPRESENTATIVES_16.txt")
    print (d)
    print (repVoting)
    makeOneNodePlot(d, repVoting)