__author__ = "Jay Patel"

import numpy as np
import random
import math
import matplotlib.pyplot as plt


"[value, row, column, index]"

def makeKbyKMap(k, dist, precinctsPerDistrict):
    statemap = []
    precPerBlock = int(precinctsPerDistrict / (k**2))
    precPerSmallRow = int(math.sqrt(precPerBlock))
    districtsqrt = int(math.sqrt(dist))
    # print (districtsqrt)
    # print (precPerBlock)
    # print (precPerSmallRow)
    for districtrow in range(districtsqrt):
        for district in range(districtsqrt):
            for bigrow in range (k):
                for block in range(k):
                    num = random.randrange(0, 100)
                    for smallrow in range(precPerSmallRow):
                        for precinct in range(precPerSmallRow):
                            row = int((districtrow * precPerSmallRow * k) + (bigrow * precPerSmallRow) + smallrow)
                            column = int((district * precPerSmallRow * k) + (block * precPerSmallRow) + precinct)
                            if num < 54:                # assign as Republican (0)
                                ind = len(statemap)
                                statemap.append([0, row, column, ind])
                            else:                       # assign as Democrat (1)
                                ind = len(statemap)
                                statemap.append([1, row, column, ind])
    return statemap

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
    percreps = [0 for i in range(600)]
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

        madepercrepdata = [0 for i in range(dist)]
        madecountdata = [0 for i in range(dist)]

        for i in range(dist):
            percrep = 0
            count = 0
            for (item, distance) in tupsList:
                if distance == i:
                    if statemap[item][0] == 0:
                        percrep += .53
                        count +=1
                    else:
                        percrep += .47
                        count += 1
            madepercrepdata[i] = percrep
            madecountdata[i] = count

            for j in range(i):
                percrep += madepercrepdata[j]
                count += madecountdata[j]

            percrep = percrep
            percreps[i] += percrep
            numPrecAtLevel[i] += count
            if dist > maxDist:
                maxDist = dist

    distances = []
    for f in range(maxDist):
        distances.append(f)
    percReps = percreps[:maxDist]
    for g in range(len(percReps)):
        percReps[g] = percReps[g] / numPrecAtLevel[g]
    print(percReps)
    print(distances)
    plt.plot(distances, percReps, color="red")
    plt.xlabel("Distance")
    plt.ylabel("Republican %")
    plt.title("Torus Circles")
    # plt.xlim(0, 60)
    # plt.ylim(.36, .73)
    # plt.yticks(np.arange(.36, .74, .03))
    plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

if __name__ == '__main__':
    statemap = makeKbyKMap(2,16, 64)
    d= createConnectedDict(statemap)
    makeAveragePlotCircles(statemap, d)