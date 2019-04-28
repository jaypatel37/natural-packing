"Analyzes how similar neighbors in Pennsylvania are to each other"

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
        if node1 == -1 or node2 == -1:
            continue
        if node1 not in d:
            connected = [node2]
            d[node1] = connected
        else:
            d[node1].append(node2)
    return d

def readVotingFile(filename):
    repVoting = [.52732 for i in range(9254)]
    f = open(filename)
    voidCount = 0
    repNum = [320 for i in range(9254)]
    totalNum = [608 for i in range(9254)]
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
    popAvg = float(totalsum) / (9253 - voidCount)
    repAvg = repTotal / totalsum
    weighted = toweigh / repTotal
    weightedDem = toweighDem / demTotal
    # demAvg = demTotal / 2691
    print ("Rep. Statewide Avg.: ", repAvg)
    print("Rep. Weighted Avg.: ", weighted)
    print("Dem. Weighted Avg.: ", weightedDem)
    # print (demAvg)
    print ("voidCount: ")
    print (voidCount)
    # print (popAvg)
    return (repVoting, repNum, totalNum)

def makeOneNodePlot(d, repVoting, repNum, precNum):
    # JUST TRY ONE NODE GRAPH FOR NOW
    queue = []
    visited = [False] * 9254
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
    for k in range(1, 9254):
        queue = []
        visited = [False] * 9254
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
    plt.title("PA Rings")
    # plt.xlim(0, 80)
    # plt.ylim(.42, .79)
    # plt.yticks(np.arange(.42, .8, .03))
    plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

def makeAveragePlotDem(d, repNum, totalNum):
    numDemsInStateAtLevel = [0 for i in range(600)]
    weightedSumsAtLevel = [0 for i in range(600)]
    maxDist = 0 # temp until we get dist
    for k in range(1, 9254):
        queue = []
        visited = [False] * 9254
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
    plt.title("PA Rings")
    # plt.xlim(0, 80)
    # plt.ylim(.42, .79)
    # plt.yticks(np.arange(.42, .8, .03))
    plt.yticks(np.arange(0, 1.1, .25))
    plt.show()

def makeAveragePlotCircles(d, repNum, totalNum):
    numRepsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
    for k in range(1, 9254):
        queue = []
        visited = [False] * 9254
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
    plt.xlabel("Distance (VTD)")
    plt.ylabel("% Chance of finding another person of the same party")
    plt.title("PA Neighbor Analysis")
    plt.xlim(0, 120)
    plt.ylim(.42, .60)
    plt.yticks(np.arange(.42, .61, .03))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()
    return distances, distances2, weightedsumsofstate, weightedsumsofstate2

def makeAveragePlotDemCircles(d, repNum, totalNum):
    numDemsInStateAtLevel = [0 for i in range(200)]
    weightedSumsAtLevel = [0 for i in range(200)]
    maxDist = 0 # temp until we get dist
    for k in range(1, 9254):
        queue = []
        visited = [False] * 9254
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
    # d = readEdgesFile("../data/PA_BORDER_LENGTHS.txt")
    # (repVoting, repNum, totalNum) = readVotingFile("../data/Penn_2016_USS.txt")
    # print (d)
    # print (repVoting)
    # makeOneNodePlot(d, repVoting,repNum ,334)
    # print (makeAveragePlot(d, repVoting))
    # makeAveragePlotCircles(d, repNum, totalNum)
    distances = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]
    distances2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]
    weightedsumsofstate = [0.5875766390912411, 0.5851737081569355, 0.5836047062819741, 0.5816885957322441, 0.5797805202993235, 0.577889655519265, 0.5759876256985216, 0.5740586047789895, 0.5723503365578945, 0.5707997199618824, 0.5694449490828212, 0.5680722817918934, 0.5667558680789052, 0.5654657055150281, 0.5641602035481323, 0.5628928137300102, 0.5616834141269348, 0.5604406502087577, 0.5592555639683329, 0.5581261352805341, 0.5569993874375302, 0.555886263281429, 0.5547811425169002, 0.5537149569122763, 0.5527022979079702, 0.5517295072868739, 0.5508135052085897, 0.549965453281975, 0.5491603572364621, 0.5484054024790352, 0.5476828652598951, 0.5469978605321758, 0.5463759078357002, 0.5458008985012381, 0.5452581445231196, 0.5447587588237909, 0.5442843756598823, 0.5438424833840387, 0.5434001745805219, 0.5429574469940645, 0.5425043943812914, 0.5420419565087614, 0.5415752692216642, 0.5410944554492363, 0.5406102130530943, 0.5401232156948963, 0.5396551749738037, 0.5391814851588901, 0.5387057971954659, 0.5382385410590915, 0.5377613261746763, 0.5372751895396538, 0.5367848088257724, 0.5362795848569623, 0.535760566928217, 0.5352278978007403, 0.5346890700611128, 0.5341449958541472, 0.5335883215257622, 0.5330165653817603, 0.5324388658471414, 0.5318550489886413, 0.5312678236886805, 0.5306786466409076, 0.5300931227523387, 0.5295170150565213, 0.5289409511231418, 0.5283733436432551, 0.5279489899309462, 0.5276098585759479, 0.5273398244236696, 0.527138642919325, 0.5270630171308767, 0.5269389434451432, 0.5268885056799827, 0.526871337842297, 0.5268039273034633, 0.5266359896584104, 0.5264725533473408, 0.5263346885138996, 0.5262640084712688, 0.526122142405308, 0.5258681615069477, 0.5254912671117307, 0.5249661360521269, 0.5244969078137416, 0.5238894024986138, 0.5232833119484521, 0.522604695254589, 0.5217432242271345, 0.5210933835166017, 0.5203060493241474, 0.5193806860563507, 0.5185168176174474, 0.5177440522835457, 0.5168411414903272, 0.5160441781915789, 0.5152150528316951, 0.514378228370261, 0.5136376576267763, 0.5129512633023469, 0.512312474102979, 0.5117950889406766, 0.5112751554652181, 0.5107932386644771, 0.5103512790429447, 0.5099623807517419, 0.5096058069967117, 0.5092485172245745, 0.5089576213522171, 0.5086881021744616, 0.5084085856706063, 0.5082030534662761, 0.5080418755874758, 0.5079052862911462, 0.5077855751851783, 0.5076849308043746, 0.5076097061351444, 0.5075555100750823, 0.5075087630187447, 0.5074713623123042, 0.5074473316928618, 0.5074318187950928, 0.5074271674046322, 0.5074182499302986, 0.5074120783826778, 0.5074082778495799, 0.5074053118494256, 0.5074004219145702, 0.5074001532309232]
    weightedsumsofstate2 = [0.5751852585954724, 0.5642357183864034, 0.5575193789580454, 0.5525224637698493, 0.5482944143539592, 0.5446069605116453, 0.5414598593782118, 0.5387425386629817, 0.5362651336713133, 0.5340279351154944, 0.5320074330322124, 0.5302444867031032, 0.5286142848915593, 0.5270591528723475, 0.5256019335598001, 0.5241731840122253, 0.5227924749713729, 0.5214856994564299, 0.5201559266578011, 0.5188146858547231, 0.5174884048102325, 0.5161539072734843, 0.5148171358494287, 0.5134675105614656, 0.5120738382825624, 0.5106705913754952, 0.5092509537886312, 0.507800501275084, 0.5063646067206422, 0.5049094949603402, 0.5034676122099544, 0.5020490394234711, 0.5006266559865868, 0.49921657105043243, 0.4978299911450432, 0.49644960101338165, 0.4951167049187294, 0.49382059851469917, 0.49258902253855513, 0.491414828153206, 0.4903063896033754, 0.48926123575674857, 0.4882786865205804, 0.4873539040581974, 0.48647576044583246, 0.4856511082976878, 0.4848537379214474, 0.4840979450715111, 0.48337619920403163, 0.48268198581122435, 0.48202934849799944, 0.48142193838555314, 0.4808619887404516, 0.4803545098048499, 0.47990763376873136, 0.47951212712741237, 0.4791604747617897, 0.47885569149138224, 0.4786035285256268, 0.4783960751326007, 0.47822948622429473, 0.47809980932537394, 0.4780067129440003, 0.47794501137616535, 0.4779112667006145, 0.47790209608422657, 0.47791912883599036, 0.4779573509746983, 0.4779711545123507, 0.4779678696335171, 0.4779382456847492, 0.47787099721167936, 0.47775145914962386, 0.4776594586456434, 0.4775060124124479, 0.47737060997353276, 0.47724629723732825, 0.47718218730333173, 0.4770887330774962, 0.477006526101518, 0.4768634932771125, 0.47675435015773243, 0.4767300730005353, 0.4767713409708306, 0.4769347069591782, 0.477065676144466, 0.47728626365301313, 0.4775125729693761, 0.4778496554850999, 0.4783263420550914, 0.4787259107365239, 0.4792708485292676, 0.4799171759688825, 0.4805572668939055, 0.4811963188674941, 0.48195785070542363, 0.4826811086901286, 0.4834661246032157, 0.4842786206471224, 0.48505938769878376, 0.48581368862405816, 0.4865295398915516, 0.4872197181528604, 0.4878848308342594, 0.4884902644604871, 0.48903691950363043, 0.48954516825960936, 0.49001683680652813, 0.4904375264624204, 0.49082111599478623, 0.49115155485878753, 0.49146765126386904, 0.4917015598795832, 0.49188781874680854, 0.4920473773945979, 0.49218002418488155, 0.49229219179186556, 0.4923752115058724, 0.4924384541293258, 0.4924880478185442, 0.4925236807902435, 0.4925475740373466, 0.492561575648779, 0.4925688249467643, 0.4925775584625378, 0.49258003024366886, 0.4925886054692681, 0.4925922185971734, 0.4925960845186665, 0.49259984676907675]
    plt.plot(distances, weightedsumsofstate, color="red")
    plt.plot(distances2, weightedsumsofstate2, color="blue")
    plt.xlabel("Distance (VTD)")
    plt.ylabel("% Chance of finding another person of the same party")
    plt.title("PA Neighbor Similarity")
    plt.xlim(0, 129)
    plt.ylim(.46, .60)
    plt.yticks(np.arange(.46, .61, .02))
    # plt.yticks(np.arange(0, 1.1, .25))
    plt.show()