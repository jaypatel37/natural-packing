"Analyzes how similar neighbors in Wisconsin are to each other"

__author__ = "Jay Patel"

import matplotlib.pyplot as plt
import numpy as np

"Reads in file containing which nodes (VTD) are connected to" \
"each other and organizeres data into a dictionary."

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

"Reads a given voting results file" \
"into a list "

def readVotingFile(filename):
    repVoting = [.558 for i in range(6896)]
    f = open(filename)
    voidCount = 0
    repNum = [176 for i in range(6896)]
    totalNum = [316 for i in range(6896)]
    totalsum = 0
    repTotal = 0
    toweigh = 0
    demTotal = 0
    toweighDem = 0
    for line in f:
        splitline = line.split()
        node = int(splitline[0])
        dem = int(splitline[1])
        rep = float(splitline[2])
        ind = int(splitline[3])
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
    popAvg = float(totalsum) / (6895 - voidCount)
    repAvg = repTotal / totalsum
    weighted = toweigh / repTotal
    weightedDem = toweighDem / demTotal
    demAvg = demTotal / totalsum
    print ("Rep. Statewide Avg.: ", repAvg)
    print("Rep. Weighted Avg.: ", weighted)
    print("Dem. Weighted Avg.: ", weightedDem)
    print (demAvg)
    print ("voidCount: ")
    print (voidCount)
    # print (popAvg)
    return (repVoting, repNum, totalNum)

"Neighbor analysis done with only one node"

def makeOneNodePlot(d, repVoting, repNum, precNum):
    # JUST TRY ONE NODE GRAPH FOR NOW
    queue = []
    visited = [False] * 6896
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

"Neighbor analysis using rings. Probabilites of finding someone of the same party" \
"that is exactly x precincts away are calculated and graphed"

def makeAveragePlotRings(d, repNum, totalNum):
    numRepsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    numDemsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevelDem = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
    for k in range(1, 6896):
        queue = []
        visited = [False] * 6896
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
            dempop = 0
            poptotal = 0
            for (item, distance) in tupsList:
                if distance == i:
                    # weightedsum += repVoting[item] * repNum[item]
                    reppop += repNum[item]
                    dempop += totalNum[item] - repNum[item]
                    poptotal += totalNum[item]
            weightedsum = (reppop / poptotal) * repNum[k]
            weightedsumDem = (dempop / poptotal) * (totalNum[k] - repNum[k])
            weightedSumsAtLevel[i] += weightedsum
            weightedSumsAtLevelDem[i] += weightedsumDem
            numRepsInStateAtLevel[i] += repNum[k]
            numDemsInStateAtLevel[i] += totalNum[k] - repNum[k]
            if dist > maxDist:
                maxDist = dist
    # print (numrepsinstateatlevel)
    # print (weightedsumsofstate)

    distances = []
    for f in range(maxDist):
        distances.append(f)
    weightedsumsofstate = weightedSumsAtLevel[:maxDist]
    weightedsumsofstateDem = weightedSumsAtLevelDem[:maxDist]
    for g in range(len(weightedsumsofstate)):
        weightedsumsofstate[g] = weightedsumsofstate[g] / numRepsInStateAtLevel[g]
        weightedsumsofstateDem[g] = weightedsumsofstateDem[g] / numDemsInStateAtLevel[g]
    print(weightedsumsofstate)
    print(weightedsumsofstateDem)
    print(distances)
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.plot(distances, weightedsumsofstateDem, color="blue")
    plt.xlabel("Distance (VTD)")
    plt.ylabel("Chance of finding another person of the same party %")
    plt.title("WI Rings")
    plt.xlim(0, 80)
    plt.ylim(.42, .79)
    plt.yticks(np.arange(.42, .8, .03))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

"Neighbor analysis using concentric circles. Probabilites of finding someone of the same party" \
"that is withing x precincts away are calculated and graphed"

def makeAveragePlotCircles(d, repNum, totalNum):
    numRepsInStateAtLevel = [0 for i in range(200)]
    numDemsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    weightedSumsAtLevelDem = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
    for k in range(1, 6896):
        queue = []
        visited = [False] * 6896
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
        madedempopdata = [0 for i in range(dist)]
        madepoptotaldata = [0 for i in range(dist)]
        for i in range(dist):
            reppop = 0
            poptotal = 0
            dempop = 0
            for (item, distance) in tupsList:
                if distance == i:
                    # weightedsum += repVoting[item] * repNum[item]
                    reppop += repNum[item]
                    poptotal += totalNum[item]
                    dempop += totalNum[item] - repNum[item]
            madereppopdata[i] = reppop
            madedempopdata[i] = dempop
            madepoptotaldata[i] = poptotal

            for j in range(i):
                reppop += madereppopdata[j]
                dempop += madedempopdata[j]
                poptotal += madepoptotaldata[j]

            weightedsum = (reppop / poptotal) * repNum[k]
            weightedSumsAtLevel[i] += weightedsum
            numRepsInStateAtLevel[i] += repNum[k]
            weightedsumdem = (dempop / poptotal) * (totalNum[k] - repNum[k])
            weightedSumsAtLevelDem[i] += weightedsumdem
            numDemsInStateAtLevel[i] += totalNum[k] - repNum[k]
            if dist > maxDist:
                maxDist = dist
    # print (numrepsinstateatlevel)
    # print (weightedsumsofstate)

    distances = []
    for f in range(maxDist):
        distances.append(f)
    weightedsumsofstate = weightedSumsAtLevel[:maxDist]
    weightedsumsofstateDem = weightedSumsAtLevelDem[:maxDist]
    for g in range(len(weightedsumsofstate)):
        weightedsumsofstate[g] = weightedsumsofstate[g] / numRepsInStateAtLevel[g]
        weightedsumsofstateDem[g] = weightedsumsofstateDem[g] / numDemsInStateAtLevel[g]
    print(weightedsumsofstate)
    print(weightedsumsofstateDem)
    print(distances)
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.plot(distances, weightedsumsofstateDem, color="blue")
    plt.xlabel("Distance (VTD)")
    plt.ylabel("% Chance of finding another person of the same party")
    plt.title("WI Neighbor Analysis")
    plt.xlim(0, 60)
    plt.ylim(.39, .79)
    plt.yticks(np.arange(.39, .8, .03))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

"Generates data for a bar graph (made in chartDrawer) that shows the distribution of " \
"vote shares across precincts (how many precincts had a Rep. voting percentage between " \
"a certain bound)"

def precVoteShare1(repNum, totalNum):
    d = {}
    votepercranges = [(0,.05),(.05, .10),(.10,.15),(.15,.20),(.20,.25),(.25,.30),(.30,.35),(.35,.40),(.40,.45),(.45,.50),(.50,.55),(.55,.60),(.60,.65),(.65,.70),(.70,.75),(.75,.80),(.80,.85),(.85,.90),(.9,.95),(.95,1)]
    for pair in votepercranges:
        d[pair] = 0
    for i in range(1, 6896):
        if totalNum == 0:
            continue
        repperc = repNum[i] / totalNum[i]
        for (x,y) in votepercranges:
            if repperc >= x and repperc < y:
                d[(x,y)] += 1
    tupList = d.items()
    newList = [[t[1],t[0]] for t in tupList]
    newList = [[t[0], t[1][1]] for t in newList]
    for i in range(len(newList)):
        newList[i][0] = newList[i][0] / 6895
    return newList

"Same goal as precVoteShare1, but does so with a traditional histogram"

def precVoteShare2(repNum, totalNum):
    data = []
    for i in range(1, 6896):
        if totalNum == 0:
            continue
        repperc = repNum[i] / totalNum[i]
        data.append(repperc)
    return data

if __name__ == '__main__':
    # d = readEdgesFile("../data/WardsBORDER_LENGTHS.txt")
    # (repVoting, repNum, totalNum) = readVotingFile("../data/WardsVOTESWSA14.txt")
    # makeAveragePlotCircles(d, repNum, totalNum)

    "After initially generating the results, they were stored here so that it was" \
    "convenient to adjust the charts without having to regenerate the data"

    distances = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]
    distances2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]
    weightedsumsofstate = [0.760664860598341, 0.7424900827551991, 0.7280481571118663, 0.715886509241524, 0.7052922698031655, 0.6957454808609799, 0.6880800298480715, 0.6813098715083772, 0.6754104752233359, 0.6702106199405687, 0.6654335640535158, 0.6610921919536763, 0.6570190289816917, 0.6530127943175285, 0.6489413666336261, 0.644848238777429, 0.6409016586536044, 0.6368749053699605, 0.633053879301205, 0.6292403943936589, 0.6255392660990212, 0.6219775226242371, 0.61843562929464, 0.614896937212132, 0.611334169530293, 0.6078320356011735, 0.6043221690827267, 0.6008663649836454, 0.597453724517937, 0.5940693406783548, 0.5907964384558493, 0.5876969198157778, 0.5847803037472139, 0.5820609583380735, 0.5795784605528459, 0.5773237116924494, 0.5752928614614469, 0.5734728178921081, 0.5718430950091768, 0.5704024369345594, 0.5691396312366901, 0.5680828664034785, 0.5671973663959562, 0.5664691339545761, 0.5658974690844789, 0.5653990651770948, 0.5650284270872494, 0.5647041203860166, 0.5644238843228729, 0.5641546745249821, 0.5638937872022686, 0.5636371511907013, 0.5634046185614909, 0.5631983224956945, 0.562996066581396, 0.5627912520806398, 0.5626377995707047, 0.5624947635963294, 0.5623777368254012, 0.5623026727216084, 0.5622345130135183, 0.5622039378177733, 0.5621856994273221, 0.562176117505139, 0.5621927059917428, 0.5621970918784371, 0.5622108910621751, 0.5622145526352078, 0.5621932690012573, 0.5621828091918236, 0.5621356158671086, 0.5620452910687649, 0.561938748919459, 0.5617911134378035, 0.5616331076960932, 0.5615046897530104, 0.5612734838770687, 0.561080104016981, 0.560834708941138, 0.5605397858819114, 0.5602894780365626, 0.5600024898743733, 0.5597107068182624, 0.5594757212985644, 0.5592758111194852, 0.5590990582823728, 0.5589495591311686, 0.5588377094053876, 0.558751078400071, 0.5586678310164365, 0.558593544768364, 0.5585401039354785, 0.5584946614444412, 0.5584760577168129, 0.5584677930716808, 0.5584671515341127, 0.5584608409149574, 0.5585523648887469, 0.5585027335182371, 0.5584361108882245, 0.5585660095051668, 0.5583766220061536, 0.5583635566994937, 0.5583556153412772]
    weightedsumsofstate2 = [0.6974564592046272, 0.6711849140991264, 0.651391755308718, 0.6358267707343306, 0.6229901405742119, 0.6108543388567815, 0.5996348209893119, 0.5898938874922088, 0.5799477165934465, 0.5703478010254969, 0.5608388335649195, 0.5513090367382752, 0.5418849225429035, 0.5324555275497691, 0.5228121376976091, 0.5130775834553727, 0.5034720124087857, 0.4942844197447464, 0.48518657748057425, 0.4765078403667931, 0.4681252316882907, 0.4602283606223335, 0.45300377008550524, 0.44641138530900804, 0.4406245041809128, 0.4354826919052095, 0.43123038883568876, 0.4278323159821675, 0.4253520467169884, 0.4236316027996028, 0.4227383524943802, 0.42239277296880867, 0.42258271755421883, 0.42309995180894316, 0.42390710944013504, 0.4248587263468702, 0.42595793141989424, 0.42722599414483386, 0.4286760837287352, 0.430202824570091, 0.4317413291649465, 0.4331476919398746, 0.43442367387059305, 0.43550038181577333, 0.4363274982512523, 0.43689504076930963, 0.43718433740309437, 0.4372954884795209, 0.4373017976640312, 0.43726446608692426, 0.437176138454048, 0.43707214472422234, 0.4369820160914631, 0.43695547947822155, 0.43696710280834483, 0.43705411137498884, 0.43716788673760987, 0.43733545109904004, 0.43751022155680275, 0.4376771535440653, 0.4378408721779801, 0.4379803928286917, 0.43809718557246446, 0.4381835658343622, 0.4382384990756208, 0.43823769766921866, 0.4381795999437197, 0.4381166845650647, 0.4379997966491483, 0.4378523890824725, 0.4377435391216613, 0.43760449982953115, 0.437471579018293, 0.43748909479300263, 0.4375595758308259, 0.4376402738684622, 0.43782184121005346, 0.43805367091360875, 0.43836858814817964, 0.4386775300806043, 0.4390166194065189, 0.43939073397070333, 0.4397356244884322, 0.44004449075231006, 0.44033579097069225, 0.440548989917716, 0.4407647451772377, 0.4409546776461092, 0.4411081675419304, 0.4412441904541708, 0.44132285979667146, 0.4413877596666072, 0.4414673292669249, 0.4415067143384196, 0.441552382127866, 0.44154904556999036, 0.441567841277414, 0.44154999099754383, 0.4415677111580944, 0.441603900602321, 0.44150719063318594, 0.44163528177060973, 0.4416364433005063, 0.44164438465872285]
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.plot(distances2, weightedsumsofstate2, color="blue")
    plt.xlabel("Distance (VTD)")
    plt.ylabel("% Chance of finding another person of the same party")
    plt.title("WI Neighbor Similarity")
    plt.xlim(0, 60)
    plt.ylim(.39, .79)
    plt.yticks(np.arange(.39, .8, .03))
    plt.show()
