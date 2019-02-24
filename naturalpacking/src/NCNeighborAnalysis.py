"Analyzes how similar neighbors in NC are to each other"

__author__ = "Jay Patel"

"Reads in file containing which nodes are connected to" \
"each other and organizes " \
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
        if node1 not in d:
            connected = [node2]
            d[node1] = connected
        else:
            d[node1].append(node2)
    return d

def readVotingFile(filename):
    repVoting = [.5 for i in range(2693)]
    f = open(filename)
    voidCount = 0
    repNum = [902 for i in range(2693)]
    totalNum = [1620 for i in range(2693)]
    totalsum = 0
    repTotal = 0
    toweigh = 0
    # demTotal = 0
    for line in f:
        splitline = line.split()
        node = int(splitline[0])
        dem = int(splitline[2])
        rep = float(splitline[3])
        ind = int(splitline[4])
        total = dem + rep + ind
        if total == 0:
            voidCount += 1
            continue
        repPerc = rep/total
        repVoting[node] = repPerc
        repNum[node] = rep
        totalNum[node] = total
        totalsum += total
        repTotal += rep
        toweigh += repPerc * rep
    #     demTotal += dem
    # popAvg = float(totalsum) / (2692 - voidCount)
    repAvg = repTotal / totalsum
    weighted = toweigh / repTotal
    # demAvg = demTotal / 2691
    print (repAvg)
    print(weighted)
    # print (demAvg)
    # print ("voidCount: ")
    # print (voidCount)
    # print (popAvg)
    return (repVoting, repNum, totalNum)

def makeOneNodePlot(d, repVoting, repNum, precNum):
    # JUST TRY ONE NODE GRAPH FOR NOW
    queue = []
    visited = [False] * 2693
    queue.append(precNum)
    visited[precNum] = True
    dist = 0
    tupsList = []
    nextLevel = []
    while len(queue) != 0:
        node = queue.pop(0)
        # print (node, " ", dist)
        tupsList.append((node,dist))
        if len(queue) == 0:
            dist += 1
            for i in nextLevel:
                queue.append(i)
                nextLevel.remove(i)
            for j in d[node]:
                if visited[j] == False:
                    queue.append(j)
                    visited[j] = True
        else:
            for i in d[node]:
                if visited[i] == False:
                    nextLevel.append(i)
                    visited[i] = True

    distances = [0 for x in range(dist)]
    percentages = [0 for x in range(dist)]
    percentages[0] = repVoting[precNum]
    for i in range(1, dist):
        weightedsum = 0
        repTotal = 0
        for (item, distance) in tupsList:
            if distance == i:
                weightedsum += repVoting[item] * repNum[item]
                repTotal += repNum[item]
        print (weightedsum, repTotal, i)
        perc = weightedsum / repTotal
        percentages[i] = perc
        distances[i] = i
    print (distances)
    print (percentages)
    plt.plot(distances, percentages, color="red")
    plt.xlabel("Distance")
    plt.ylabel("Republican %")
    plt.yticks(np.arange(0, 1.1, .25))
    plt.show()


def makeAveragePlot(d, repVoting, repNum, totalNum):
    numRepsInStateAtLevel = [0 for i in range(1, 2693)]
    weightedSumsAtLevel = [0 for i in range(1, 2693)]
    for k in range(1, 2693):
        queue = []
        visited = [False] * 2693
        queue.append(k)
        visited[k] = True
        dist = 0
        tupsList = []
        nextLevel = []
        while len(queue) != 0:
            node = queue.pop(0)
            # print (node, " ", dist)
            tupsList.append((node, dist))
            if len(queue) == 0:
                dist += 1
                for i in nextLevel:
                    queue.append(i)
                    nextLevel.remove(i)
                if node not in d:
                    continue
                for j in d[node]:
                    if visited[j] == False:
                        queue.append(j)
                        visited[j] = True
            else:
                for n in d[node]:
                    if visited[n] == False:
                        nextLevel.append(n)
                        visited[n] = True

        # distances = [0 for x in range(dist)]
        # percentages = [0 for x in range(dist)]
        # percentages[0] = repVoting[k]
        # weightedsumsofstate[0] += repVoting[k] * repNum[k]
        # numrepsinstateatlevel[0] += repNum[k]
        for i in range(dist):
            reppop = 0
            poptotal = 0
            for (item, distance) in tupsList:
                if distance == i:
                    # weightedsum += repVoting[item] * repNum[item]
                    reppop += repNum[item]
                    poptotal += totalNum[item]
            weightedsum = (reppop / poptotal) * repNum[k]
            weightedSumsAtLevel[i] += weightedsum
            numRepsInStateAtLevel[i] += repNum[k]
    # print (numrepsinstateatlevel)
    # print (weightedsumsofstate)
    distances = [0 for b in range(88)]
    for a in range(len(numRepsInStateAtLevel)):
        if weightedSumsAtLevel[a] != 0:
            distances[a] = a
    weightedsumsofstate = weightedSumsAtLevel[:88]
    # print(weightedsumsofstate)
    # print(distances)
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.xlabel("Distance")
    plt.ylabel("Republican %")
    plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

def makeAveragePlotDem(d, repVoting, repNum, totalNum):
    numrepsinstateatlevel = [0 for i in range(2693)]
    weightedsumsofstate = [0 for i in range(2693)]
    for k in range(1, 2693):
        queue = []
        visited = [False] * 2693
        queue.append(k)
        visited[k] = True
        dist = 0
        tupsList = []
        nextLevel = []
        while len(queue) != 0:
            node = queue.pop(0)
            # print (node, " ", dist)
            tupsList.append((node, dist))
            if len(queue) == 0:
                dist += 1
                for i in nextLevel:
                    queue.append(i)
                    nextLevel.remove(i)
                if node not in d:
                    continue
                for j in d[node]:
                    if visited[j] == False:
                        queue.append(j)
                        visited[j] = True
            else:
                for n in d[node]:
                    if visited[n] == False:
                        nextLevel.append(n)
                        visited[n] = True

        for i in range(dist):
            weightedsum = 0
            demTotal = 0
            for (item, distance) in tupsList:
                if distance == i:
                    # weightedsum += repVoting[item] * repNum[item]
                    weightedsum += totalNum[item] - repNum[item]
                    demTotal += totalNum[item]
            weightedsumsofstate[i] += weightedsum
            numrepsinstateatlevel[i] += demTotal
    print (numrepsinstateatlevel)
    print (weightedsumsofstate)
    distances = [0 for b in range(98)]
    for a in range(len(numrepsinstateatlevel)):
        if weightedsumsofstate[a] != 0:
            weightedsumsofstate[a] = weightedsumsofstate[a]/numrepsinstateatlevel[a]
            distances[a] = a
    weightedsumsofstate = weightedsumsofstate[:98]
    print(weightedsumsofstate)
    print(distances)
    plt.plot(distances, weightedsumsofstate, color="blue")
    plt.xlabel("Distance")
    plt.ylabel("Democratic %")
    plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

if __name__ == '__main__':
    d = readEdgesFile("../data/NC_Edges_Lengths.txt")
    (repVoting, repNum, totalNum) = readVotingFile("../data/VTDLevel_USHOUSEOFREPRESENTATIVES_16.txt")
    # print (d)
    # print (repVoting)
    makeOneNodePlot(d, repVoting,repNum ,334)
    # print (makeAveragePlot(d, repVoting))
    # makeAveragePlot(d, repVoting, repNum, totalNum)