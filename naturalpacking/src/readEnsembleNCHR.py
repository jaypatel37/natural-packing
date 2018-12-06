

def read(filename):
        d = {}
        d2 = {}
        f = open(filename)
        distCount = 0
        for line in f:
            line = line.strip()
            (dist, perc) = line.split("\t")
            dist = int(dist)
            perc = float(perc)
            if dist not in d:
                d[dist] = perc
            else:
                d[dist] += perc
            if perc > .5:
                distCount += 1
            if dist == 13:
                if distCount not in d2:
                    d2[distCount] = 1
                else:
                    d2[distCount] += 1
                distCount = 0
        for i in range(1, 14):
            d[i] = d[i] / 24000
        info = d.items()
        info2 = d2.items()
        info2 = [[t[0],t[1]] for t in info2]

        return (info, info2)

def createList(counts):
    ans = []
    for item in counts:
        num = item[0]
        amount = item[1]
        for i in range(amount):
            ans.append(num)
    return ans

def organizeForBarGraph(counts):
    for item in counts:
        num = item[0]
        amount = item[1]
        amount = amount / 24000
        item[0] = amount
        item[1] = num
    return counts

if __name__ == '__main__':
    (avgs, counts) = read("../data/MCMCElectionMargins_ALLNEW_USHOUSEOFREPRESENTATIVES_16_Sorted")
    print (avgs)
    info = [[t[0], t[1]] for t in avgs]
    demvote = 0
    for item in avgs:
        demvote += item[1]
    demvote = demvote /13
    print (demvote)
    print (counts)
    sum = 0
    for thing in counts:
        sum += thing[0] * thing[1]
    sum = sum /24000
    print(sum)
    ansList = createList(counts)
    print (ansList)
