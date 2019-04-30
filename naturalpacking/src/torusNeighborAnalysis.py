__author__ = "Jay Patel"

import numpy as np
import random
import math
import matplotlib.pyplot as plt


"Creates the kxk map. In order to create the map with the correct indices, it is broken down" \
"into many nested iterations"

"Format of each entry is [value, row, column, index]"

def makeKbyKMap(k, dist, precinctsPerDistrict):
    statemap = []
    precPerBlock = int(precinctsPerDistrict / (k**2))
    precPerSmallRow = int(math.sqrt(precPerBlock))
    districtsqrt = int(math.sqrt(dist))
    demAssignFlag = True        # Used to determine if 4 or 5 precincts should be assigned to a Dem block if we have 8 precincts.
    reassignFlag = False        # Used to determine if we need to flip the demAssignFlag. Avg # of precincts in 8 prec Dem blocks should be ~4.5
    # print (districtsqrt)
    print (precPerBlock)
    # print (precPerSmallRow)
    for districtrow in range(districtsqrt):
        for district in range(districtsqrt):
            for bigrow in range (k):
                for block in range(k):
                    num = random.randrange(0, 100)
                    repCount = 0
                    demCount = 0
                    if reassignFlag:
                        demAssignFlag = not demAssignFlag
                        reassignFlag = False
                    for smallrow in range(precPerSmallRow):
                        for precinct in range(precPerSmallRow):
                            row = int((districtrow * precPerSmallRow * k) + (bigrow * precPerSmallRow) + smallrow)
                            column = int((district * precPerSmallRow * k) + (block * precPerSmallRow) + precinct)
                            ind = len(statemap)
                            if num < 53:                # assign as Republican Block(61.5% Rep)
                                if precPerBlock == 8:
                                    if repCount < 5:    # still need more Reps in this block
                                        statemap.append([0, row, column, ind])
                                        repCount += 1
                                    else:               # have 5 Reps already, assign this precinct as Dem
                                        statemap.append([1, row, column, ind])
                                if precPerBlock == 16:
                                    if repCount < 10:  # still need more Reps in this block
                                        statemap.append([0, row, column, ind])
                                        repCount += 1
                                    else:  # have 10 Reps already, assign this precinct as Dem
                                        statemap.append([1, row, column, ind])
                            else:                       # assign as Democrat Block (44% Rep)
                                if precPerBlock == 8:
                                    reassignFlag = True
                                    if demAssignFlag:   # assigning 5 Dems this time (alternating flag used to make numbers more accurate)
                                        if demCount < 5:    # still need more Dems in this block
                                            statemap.append([1, row, column, ind])
                                            demCount += 1
                                        else:
                                            statemap.append([0, row, column, ind])
                                    else:               # assigning 4 Dems
                                        if demCount < 4:    # still need more Dems in this block
                                            statemap.append([1, row, column, ind])
                                            demCount += 1
                                        else:               # have 4 Dems already, assign this precinct as Rep
                                            statemap.append([0, row, column, ind])
                                if precPerBlock == 16:
                                    if demCount < 9:  # still need more Dems in this block
                                        statemap.append([1, row, column, ind])
                                        demCount += 1
                                    else:  # have 10 Dems already, assign this precinct as Dem
                                        statemap.append([0, row, column, ind])
    return statemap

"Makes connected dictionary using the IDs of precincts in a given statemap"

def createConnectedDict(statemap):
    d = {}
    for prec in statemap:
        d[prec[3]] = []
        for i in statemap:
            if (abs(statemap[prec[3]][1] - i[1]) + abs(statemap[prec[3]][2] - i[2])) == 1:    # i is above, below, or besides prec
                d[prec[3]].append(i[3])
            if (abs(statemap[prec[3]][1] - i[1]) == 1) and (abs(statemap[prec[3]][2] - i[2]) == 1):   # i is diagonal from prec
                d[prec[3]].append(i[3])
    return d



def makeAveragePlotCircles(statemap, d):
    numPrecAtLevel = [0 for i in range(600)]
    repCounts = [0 for i in range(600)]
    demCounts = [0 for i in range(600)]
    maxDist = 0 # temp until we get dist
    numprec = len(statemap)
    for k in range(numprec):
        queue = []
        visited = [False] * numprec
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

        maderepcountdata = [0 for i in range(dist)]
        madedemcountdata = [0 for i in range(dist)]
        madecountdata = [0 for i in range(dist)]

        for i in range(dist):
            repcount = 0
            demcount = 0
            count = 0
            for (item, distance) in tupsList:
                if distance == i:
                    if statemap[item][0] == 0:
                        repcount += 1
                    if statemap[item][0] == 1:
                        demcount += 1
                    count +=1
            maderepcountdata[i] = repcount
            madedemcountdata[i] = demcount
            madecountdata[i] = count

            for j in range(i):
                repcount += maderepcountdata[j]
                demcount += madedemcountdata[j]
                count += madecountdata[j]

            repCounts[i] += repcount
            demCounts[i] += demcount
            numPrecAtLevel[i] += count
            if dist > maxDist:
                maxDist = dist

    distances = []
    for f in range(maxDist):
        distances.append(f)
    repCounts = repCounts[:maxDist]
    demCounts = demCounts[:maxDist]
    for g in range(len(repCounts)):
        repCounts[g] = repCounts[g] / numPrecAtLevel[g]
        demCounts[g] = demCounts[g] / numPrecAtLevel[g]
    print(repCounts)
    print(demCounts)
    print(distances)
    plt.plot(distances, repCounts, color="red")
    plt.plot(distances, demCounts, color="blue")
    plt.xlabel("Distance")
    plt.ylabel("% Chance of finding another person of the same party")
    plt.title("Torus Neighbor Similarity")
    plt.xlim(0, 60)
    plt.ylim(.44, .56)
    plt.yticks(np.arange(.44, .57, .02))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

if __name__ == '__main__':
    statemap = makeKbyKMap(4,16, 256)
    d= createConnectedDict(statemap)
    makeAveragePlotCircles(statemap, d)