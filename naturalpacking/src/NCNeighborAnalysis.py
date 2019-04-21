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
    demTotal = 0
    toweighDem = 0
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
        demTotal += dem
        toweigh += repPerc * rep
        toweighDem += (1 - repPerc) * dem
    #     demTotal += dem
    # popAvg = float(totalsum) / (2692 - voidCount)
    repAvg = repTotal / totalsum
    weighted = toweigh / repTotal
    weightedDem = toweighDem / demTotal
    # demAvg = demTotal / 2691
    print("Rep. Statewide Avg.: ", repAvg)
    print("Rep. Weighted Avg.: ", weighted)
    print("Dem. Weighted Avg.: ", weightedDem)
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
    numRepsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
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
            if dist > maxDist:
                maxDist = dist
    # print (numrepsinstateatlevel)
    # print (weightedsumsofstate)

    distances = []
    for f in range(maxDist):
        distances.append(f)
    weightedsumsofstate = weightedSumsAtLevel[:maxDist]
    for g in range(len(weightedsumsofstate)):
        weightedsumsofstate[g] = weightedsumsofstate[g] / numRepsInStateAtLevel[g]
    print(weightedsumsofstate)
    print(distances)
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.xlabel("Distance")
    plt.ylabel("Republican %")
    plt.title("NC Rings")
    plt.xlim(0, 60)
    plt.ylim(.5, .65)
    plt.yticks(np.arange(.5, .65, .03))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

def makeAveragePlotDem(d, repVoting, repNum, totalNum):
    numDemsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
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
            dempop = 0
            poptotal = 0
            for (item, distance) in tupsList:
                if distance == i:
                    # weightedsum += repVoting[item] * repNum[item]
                    dempop += totalNum[item] - repNum[item]
                    poptotal += totalNum[item]
            weightedsum = (dempop / poptotal) * (totalNum[k] - repNum[k])
            weightedSumsAtLevel[i] += weightedsum
            numDemsInStateAtLevel[i] += totalNum[k] - repNum[k]
            if dist > maxDist:
                maxDist = dist
    # print (numrepsinstateatlevel)
    # print (weightedsumsofstate)

    distances = []
    for f in range(maxDist):
        distances.append(f)
    weightedsumsofstate = weightedSumsAtLevel[:maxDist]
    for g in range(len(weightedsumsofstate)):
        weightedsumsofstate[g] = weightedsumsofstate[g] / numDemsInStateAtLevel[g]
    print(weightedsumsofstate)
    print(distances)
    ax = plt.plot(distances, weightedsumsofstate, color="blue")
    # print (ax)
    # ax.hlines(0.5338738556976275, 0, 1)
    # plt.plot([0,1],[0.5338738556976275])
    # ax.axhline(0.5338738556976275, 0, 1)
    # ax.axhline(0.6149895769827122, 0, 1)
    plt.xlabel("Distance")
    plt.ylabel("Democrat %")
    plt.title("NC Rings")
    plt.xlim(0, 60)
    plt.ylim(.36, .57)
    plt.yticks(np.arange(.36, .58, .03))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

def makeAveragePlotCircles(d, repVoting, repNum, totalNum):
    numRepsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
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

        madereppopdata = [0 for i in range(dist)]
        madepoptotaldata = [0 for i in range(dist)]
        for i in range(dist):
            reppop = 0
            poptotal = 0
            for (item, distance) in tupsList:
                if distance == i:
                    # weightedsum += repVoting[item] * repNum[item]
                    reppop += repNum[item]
                    poptotal += totalNum[item]
            madereppopdata[i] = reppop
            madepoptotaldata[i] = poptotal

            for j in range(i):
                reppop += madereppopdata[j]
                poptotal += madepoptotaldata[j]

            weightedsum = (reppop / poptotal) * repNum[k]
            weightedSumsAtLevel[i] += weightedsum
            numRepsInStateAtLevel[i] += repNum[k]
            if dist > maxDist:
                maxDist = dist
    # print (numrepsinstateatlevel)
    # print (weightedsumsofstate)

    distances = []
    for f in range(maxDist):
        distances.append(f)
    weightedsumsofstate = weightedSumsAtLevel[:maxDist]
    for g in range(len(weightedsumsofstate)):
        weightedsumsofstate[g] = weightedsumsofstate[g] / numRepsInStateAtLevel[g]
    print(weightedsumsofstate)
    print(distances)
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.xlabel("Distance")
    plt.ylabel("Republican %")
    plt.title("NC Circles")
    plt.xlim(0,60)
    plt.ylim(.5, .62)
    plt.yticks(np.arange(.5, .63, .03))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

def makeAveragePlotDemCircles(d, repVoting, repNum, totalNum):
    numDemsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
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

        madedempopdata = [0 for i in range(dist)]
        madepoptotaldata = [0 for i in range(dist)]
        for i in range(dist):
            dempop = 0
            poptotal = 0
            for (item, distance) in tupsList:
                if distance == i:
                    # weightedsum += repVoting[item] * repNum[item]
                    dempop += totalNum[item] - repNum[item]
                    poptotal += totalNum[item]
            madedempopdata[i] = dempop
            madepoptotaldata[i] = poptotal

            for j in range(i):
                dempop += madedempopdata[j]
                poptotal += madepoptotaldata[j]

            weightedsum = (dempop / poptotal) * (totalNum[k] - repNum[k])
            weightedSumsAtLevel[i] += weightedsum
            numDemsInStateAtLevel[i] += totalNum[k] - repNum[k]
            if dist > maxDist:
                maxDist = dist
    # print (numrepsinstateatlevel)
    # print (weightedsumsofstate)

    distances = []
    for f in range(maxDist):
        distances.append(f)
    weightedsumsofstate = weightedSumsAtLevel[:maxDist]
    for g in range(len(weightedsumsofstate)):
        weightedsumsofstate[g] = weightedsumsofstate[g] / numDemsInStateAtLevel[g]
    print(weightedsumsofstate)
    print(distances)
    ax = plt.plot(distances, weightedsumsofstate, color="blue")
    # print (ax)
    # ax.hlines(0.5338738556976275, 0, 1)
    # plt.plot([0,1],[0.5338738556976275])
    # ax.axhline(0.5338738556976275, 0, 1)
    # ax.axhline(0.6149895769827122, 0, 1)
    plt.xlabel("Distance")
    plt.ylabel("Democrat %")
    plt.title("NC Circles")
    plt.xlim(0,60)
    plt.ylim(.45,.57)
    plt.yticks(np.arange(.45, .58, .03))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()


if __name__ == '__main__':
    d = readEdgesFile("../data/NC_Edges_Lengths.txt")
    (repVoting, repNum, totalNum) = readVotingFile("../data/VTDLevel_USHOUSEOFREPRESENTATIVES_16.txt")
    # print (d)
    # print (repVoting)
    # makeOneNodePlot(d, repVoting,repNum ,334)
    # print (makeAveragePlot(d, repVoting))
    makeAveragePlotDemCircles(d, repVoting, repNum, totalNum)