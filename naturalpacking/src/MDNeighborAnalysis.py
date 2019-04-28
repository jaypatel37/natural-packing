"Analyzes how similar neighbors in Maryland are to each other"

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
        if node1 == -1:
            continue
        if node1 not in d:
            connected = [node2]
            d[node1] = connected
        else:
            d[node1].append(node2)
    return d

def readVotingFile(filename):
    repVoting = [.435 for i in range(1849)]
    f = open(filename)
    voidCount = 0
    repNum = [308 for i in range(1849)]
    totalNum = [709 for i in range(1849)]
    totalsum = 0
    repTotal = 0
    toweigh = 0
    demTotal = 0
    toweighDem = 0
    for line in f:
        splitline = line.split()
        if splitline[0] == "Precinct":
            continue
        node = int(splitline[0])
        dem = int(splitline[1])
        rep = float(splitline[2])
        total = dem + rep
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
    popAvg = float(totalsum) / (1849 - voidCount)
    repAvg = repTotal / totalsum
    weighted = toweigh / repTotal
    weightedDem = toweighDem / demTotal
    print ("Rep. Statewide Avg.: ", repAvg)
    print("Rep. Weighted Avg.: ", weighted)
    print("Dem. Weighted Avg.: ", weightedDem)
    # print ("voidCount: ")
    # print (voidCount)
    # print (popAvg)
    return (repVoting, repNum, totalNum)

def makeOneNodePlot(d, repVoting, repNum, precNum):
    # JUST TRY ONE NODE GRAPH FOR NOW
    queue = []
    visited = [False] * 1849
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


def makeAveragePlot(d, repNum, totalNum):
    numRepsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
    for k in range(1849):
        queue = []
        visited = [False] * 1849
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
    plt.title("MD Rings")
    plt.xlim(0, 60)
    plt.ylim(.36, .73)
    plt.yticks(np.arange(.36, .74, .03))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

def makeAveragePlotDem(d, repNum, totalNum):
    numDemsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
    for k in range(1849):
        queue = []
        visited = [False] * 1849
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
    plt.plot(distances, weightedsumsofstate, color="blue")
    plt.xlabel("Distance")
    plt.ylabel("Democrat %")
    plt.title("MD Rings")
    plt.xlim(0, 60)
    plt.ylim(.25, .68)
    plt.yticks(np.arange(.25, .69, .03))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

def makeAveragePlotCircles(d, repNum, totalNum):
    numRepsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
    for k in range(1849):
        queue = []
        visited = [False] * 1849
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
    distances2, weightedsumsofstate2 = makeAveragePlotDemCircles(d, repNum, totalNum)
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.plot(distances2, weightedsumsofstate2, color="blue")
    plt.xlabel("Distance")
    plt.ylabel("% Chance of finding another person of the same party")
    plt.title("MD Neighbor Similarity")
    plt.xlim(0, 60)
    plt.ylim(.39, .67)
    plt.yticks(np.arange(.39, .68, .03))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

def makeAveragePlotDemCircles(d, repNum, totalNum):
    numDemsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
    for k in range(1849):
        queue = []
        visited = [False] * 1849
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
    return distances, weightedsumsofstate

if __name__ == '__main__':
    # d = readEdgesFile("../data/MDPrecinctBORDER_LENGTHS.txt")
    # (repVoting, repNum, totalNum) = readVotingFile("../data/MDPrecinctHOUSE14.txt")
    # makeAveragePlotCircles(d, repNum, totalNum)
    distances = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
    distances2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
    weightedsumsofstate = [0.550934134646445, 0.5461023980880709, 0.5414434266154159, 0.5376325775221547, 0.5332096037446102, 0.5284283912405005, 0.5239328619591388, 0.5187723033157321, 0.5132741057650156, 0.5080775338048128, 0.5024459265640845, 0.4968137468672436, 0.49096821391813966, 0.48530179009721675, 0.4800477500479281, 0.4751432156293702, 0.4706679907645281, 0.46662809803101324, 0.4630735003343593, 0.4600325340066692, 0.4575069853160596, 0.4553149806684036, 0.453382714962212, 0.4514211437624425, 0.44941612519906016, 0.4473756016642488, 0.44534771120562927, 0.44333718164911007, 0.44135094150293264, 0.4394567107946323, 0.43760344298032267, 0.43597309099056863, 0.4346290674806672, 0.43354570809564, 0.4326574116610226, 0.43196003845380715, 0.4315183367831425, 0.4312275377220314, 0.4311347955080086, 0.4311614927113838, 0.4312720616364463, 0.43146746851408196, 0.43170761905434135, 0.43198235226559917, 0.432232787119499, 0.432460292589538, 0.43265295354800515, 0.43283640718617894, 0.4329994804785634, 0.4331494196866229, 0.43322236492615984, 0.4333151227480106, 0.43338172741614633, 0.4333944012060143, 0.43340013240369246, 0.43343619927602695, 0.43332831516426423, 0.4333264470823603, 0.43323684907975407, 0.4332858775431627, 0.4334098044427439, 0.4335242898359633, 0.4336393109101981, 0.4337044880484477, 0.43380182619606344, 0.43390453501515414, 0.4339388434853109, 0.4339081526729504, 0.4339922969622542, 0.43400808754604325, 0.43416806582646394, 0.43426104508794333, 0.43426785999463313, 0.434432488299998, 0.4346400339889456, 0.43475334848546876, 0.43483126711968695, 0.4349642798439057, 0.4349584566676501, 0.4350035701426226]
    weightedsumsofstate2 = [0.6542099169609826, 0.648572317767276, 0.6431041886282575, 0.6378073771860404, 0.6325083200505508, 0.6275470357622753, 0.6224439848210075, 0.6173583800313098, 0.612464089935238, 0.6075011227472019, 0.602945333263766, 0.5982080194214694, 0.5942090388320823, 0.5903173125130099, 0.5868713168175264, 0.5837584364711651, 0.5809891265436786, 0.5785660537479729, 0.5764823673120667, 0.5748088411006873, 0.5734687114647716, 0.5723687833042281, 0.5715470824701699, 0.571105384487208, 0.5709848903611844, 0.5711548509809846, 0.5714777263878852, 0.5718679601821652, 0.5722603841296867, 0.5726205820883349, 0.5728775036370617, 0.5730430308369203, 0.573043552037949, 0.5729114154026711, 0.5726992812916702, 0.5724246670334983, 0.5720326523324983, 0.571611062540746, 0.5711047090397143, 0.5706172752656093, 0.5701200663030986, 0.5696353081708669, 0.569157679281264, 0.568706255383165, 0.5683015861522248, 0.5679519792299729, 0.5676328771230829, 0.5673471938121786, 0.5670935463153527, 0.5668817074908837, 0.5667142111239992, 0.5665486358158297, 0.5664345223578932, 0.5663586115582289, 0.5662812288457569, 0.5662068630336394, 0.5662065696835005, 0.5661457091633134, 0.5661526162238698, 0.5661099163321036, 0.5660627118847675, 0.5659983356489234, 0.5659386640336765, 0.5659104211866526, 0.5658924966283811, 0.5658285237160354, 0.5658733784012495, 0.5659371978759236, 0.5659311432293324, 0.5659344029852008, 0.5658230698317377, 0.5657418139194159, 0.5657374276154666, 0.5656112162100492, 0.5653813438611314, 0.565264881483458, 0.565177433353873, 0.565050065468823, 0.5650199272722023, 0.5649964298573774]
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.plot(distances2, weightedsumsofstate2, color="blue")
    plt.xlabel("Distance (VTD)")
    plt.ylabel("% Chance of finding another person of the same party")
    plt.title("MD Neighbor Similarity")
    plt.xlim(0, 60)
    plt.ylim(.39, .67)
    plt.yticks(np.arange(.39, .68, .03))
    plt.show()
