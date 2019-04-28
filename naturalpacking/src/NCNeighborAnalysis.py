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
    distances2, weightedsumsofstate2 = makeAveragePlotDemCircles(d, repVoting, repNum, totalNum)
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.plot(distances2, weightedsumsofstate2, color="blue")
    plt.xlabel("Distance (VTD)")
    plt.ylabel("% Chance of finding another person of the same party")
    plt.title("NC Neighbor Similarity")
    plt.xlim(0,60)
    plt.ylim(.44, .62)
    plt.yticks(np.arange(.44, .63, .02))
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
    return distances, weightedsumsofstate

# def precVoteShare1(repNum, totalNum):
#     d = {}
#     votepercranges = [(0,.05),(.05, .10),(.10,.15),(.15,.20),(.20,.25),(.25,.30),(.30,.35),(.35,.40),(.40,.45),(.45,.50),(.50,.55),(.55,.60),(.60,.65),(.65,.70),(.70,.75),(.75,.80),(.80,.85),(.85,.90),(.9,.95),(.95,1)]
#     for pair in votepercranges:
#         d[pair] = 0
#     for i in range(1, 2693):
#         if totalNum == 0:
#             continue
#         repperc = repNum[i] / totalNum[i]
#         for (x,y) in votepercranges:
#             if repperc >= x and repperc < y:
#                 d[(x,y)] += 1
#     tupList = d.items()
#     newList = [[t[1],t[0]] for t in tupList]
#     newList = [[t[0], t[1][1]] for t in newList]
#     for i in range(len(newList)):
#         newList[i][0] = newList[i][0] / 2692
#     return newList

def precVoteShare2(repNum, totalNum):
    data = []
    for i in range(1, 2693):
        if totalNum == 0:
            continue
        repperc = repNum[i] / totalNum[i]
        data.append(repperc)
    return data


if __name__ == '__main__':
    # d = readEdgesFile("../data/NC_Edges_Lengths.txt")
    # (repVoting, repNum, totalNum) = readVotingFile("../data/VTDLevel_USHOUSEOFREPRESENTATIVES_16.txt")
    # makeAveragePlotCircles(d, repVoting, repNum, totalNum)
    distances = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]
    distances2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]
    weightedsumsofstate = [0.6149463874129587, 0.6010293650202914, 0.5936438569210257, 0.5864220431337116, 0.5805185532754685, 0.576006209452862, 0.5710899140896456, 0.5670645445415888, 0.5634018582662773, 0.5604193375867251, 0.5582358033827333, 0.5563604876517545, 0.5548915489840744, 0.5537839404077757, 0.5531141277783982, 0.5523812366472229, 0.5518576598570476, 0.5512802736444284, 0.5506749758483495, 0.5499028895384562, 0.5488206159976226, 0.5476743990593799, 0.5464758706921596, 0.5451753555999875, 0.5438518842498221, 0.5424372324323834, 0.5410895476226126, 0.5397388930391834, 0.5385235733227457, 0.5374194357980074, 0.5364464942936553, 0.5356609775387587, 0.5349664711374549, 0.5344261189176108, 0.5339702270195792, 0.5335986600224749, 0.5332566878460738, 0.5329807066108467, 0.5327504761524163, 0.5326051013734445, 0.5325383970359172, 0.5325216760682795, 0.5325415644542354, 0.5325688841269736, 0.5325945557148607, 0.5326476373464215, 0.5327004522183577, 0.5327467027881754, 0.5327926434268313, 0.5328281321973116, 0.5328557786889935, 0.5328681644261818, 0.5328527480498685, 0.5328288034144938, 0.5327894508949855, 0.5327419080718502, 0.5326895050498902, 0.5326501558442744, 0.5326343468425966, 0.5326039696908076, 0.5325836733543194, 0.5325738002886533, 0.5325544451523583, 0.5325721800114421, 0.5326153061654536, 0.5326691902784529, 0.5326965164311559, 0.5327526276983958, 0.5327944949831821, 0.5328367078946891, 0.5328777962880155, 0.5329228818934325, 0.5329733820932013, 0.5330237537790136, 0.5330721575541055, 0.5331656943947829, 0.5332195554628778, 0.5332752176643397, 0.5333272745283096, 0.5333889737239922, 0.5334408272680939, 0.5334647186919682, 0.5334949849620637, 0.5335437646034618, 0.5335851404466255, 0.5336351601457616, 0.5336716932466797, 0.5337077810443497, 0.5337428080454749, 0.533763639714695, 0.5337803417816703, 0.5337338948896647, 0.5336625956904262, 0.5337359793050411, 0.5338009561550194, 0.5338385796826954, 0.5338490075750965, 0.5338738556976275]
    weightedsumsofstate2 = [0.5589530211233388, 0.538650483933524, 0.524603039315367, 0.5145979727214133, 0.5072238044487332, 0.4999789537897175, 0.4947467662442004, 0.4900549640161064, 0.4857875748620321, 0.482137667296901, 0.4789455039956947, 0.4764742848244445, 0.4744054331324877, 0.47257028901651915, 0.4707961016954283, 0.4693293809706411, 0.4678772453866201, 0.4665740295269249, 0.46529952178289824, 0.46431782050902715, 0.46371908743054663, 0.46330606566605254, 0.4631811607835526, 0.4633105235772872, 0.46364668343015447, 0.4642314213718048, 0.4648403556393367, 0.4655449078794599, 0.4662162532441723, 0.46689545959892165, 0.46750092323512904, 0.46801673470529986, 0.4684461077683163, 0.4687276386701216, 0.46891484685337104, 0.46900790973851464, 0.4690618604890482, 0.469033334638098, 0.468964637797513, 0.4688113942113818, 0.46860884306950296, 0.46839321684753615, 0.4681863013615649, 0.4680019743364807, 0.4678582333936767, 0.46772423231839355, 0.4676132181870716, 0.4675486277710692, 0.4674959957612091, 0.4674579173860371, 0.4674395255620197, 0.4674287320825679, 0.46742816043185176, 0.46743400291607784, 0.46745532874415635, 0.4674671682527243, 0.46747689536129444, 0.4674760156088188, 0.46745481531749467, 0.4674459390269495, 0.46743876110382254, 0.4674336049545969, 0.467427050516756, 0.4673787754807976, 0.46733790122857605, 0.4672761706957698, 0.4672530783571477, 0.4672012107440319, 0.4671344230124891, 0.46708032011559725, 0.4670321363320689, 0.46699144915670926, 0.4669160126843395, 0.4668625164952139, 0.46681069723076946, 0.46671606836157625, 0.4666724740338106, 0.46663183620216875, 0.4665721755987248, 0.4665236811949591, 0.4664886298936247, 0.46648074370473697, 0.46645189054959285, 0.4664124852777964, 0.4663792152289516, 0.46632804292521196, 0.4662845953293524, 0.4662530626925204, 0.46623353552651603, 0.4662068093766515, 0.4661860365282193, 0.46622160230442744, 0.46630145914791055, 0.4662343148722781, 0.4661931643919357, 0.46616142031730456, 0.4661509924249035, 0.46612614430237254]
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.plot(distances2, weightedsumsofstate2, color="blue")
    plt.xlabel("Distance (VTD)")
    plt.ylabel("% Chance of finding another person of the same party")
    plt.title("NC Neighbor Similarity")
    plt.xlim(0, 60)
    plt.ylim(.44, .62)
    plt.yticks(np.arange(.44, .63, .02))
    plt.show()