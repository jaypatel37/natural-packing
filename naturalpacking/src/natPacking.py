"Various starting functions"

__author__ = "Jay Patel"

import random
import math
import numpy as np
from src import torusMap

"Very first map generator, creates a map with dist number of " \
"districts with prec number of precincts in each one. Each precinct" \
"is marked as urban, rural, or suburban based on real life NC " \
"proportions"

def setUp(dist, prec):
    statemap = [[0 for x in range(prec)] for x in range(dist)]
    for i in range(dist):
        for j in range (prec):
            num = random.randrange(0,100)
            if (num < 37):
                statemap[i][j] = 2 #mark as urban d
            elif(num >= 37 and num < 63):
                statemap[i][j] = 1 #mark as suburban
            else:
                statemap[i][j] = 0 #mark as rural
    return statemap

"Basic city dropping algorithm, drops a 3x3 city at a random location" \
"within a district"

#precincts must be a perfect squarepc

def droppingCities(districts, precincts, cities):
    statemap =[[0 for x in range(precincts)]for x in range(districts)]
    added = [0] * districts
    for i in range(cities):
        num = random.randrange(districts)
        while added[num] == 2:
            num = random.randrange(districts)
        added[num] = 2
        distn = statemap[num] # distn is the district we are adding the city to
        n = math.sqrt(len(distn))
        n = int(n)
        max = (n-1)*n - 1
        min = n+1
        num2 = random.randrange(min,max)
        while num2 % n == 0 or (num2 +1) % n ==0:
            num2 = random.randrange(min, max)
        distn[num2] = 2
        distn[num2 - 1] = 2
        distn[num2 - (n - 1)] = 2
        distn[num2 - n] = 1
        distn[num2 - (n + 1)] = 2
        distn[num2 + 1] = 1
        distn[num2 + (n - 1)] = 2
        distn[num2 + n] = 1
        distn[num2 + (n + 1)] = 2
    return statemap

"Upgraded city dropping algorithm that drops cities of size " \
"size by size, this includes a suburban area wrapping around the" \
"main city"
# precincts is TOTAL number of precincts
# size is total metropolitan area (urban and suburban)
# rings is how many suburban rings should go around city
def droppingCities2(precincts, cities, size, rings):
    precmap = [0 for x in range(precincts)]
    avoid = set([])
    n = math.sqrt(precincts)
    n = int(n)
    for i in range(n - size):
        for j in range(n-size+1, n):
            avoid.add(j + (i*n))
    for a in range(cities):
        num = random.randrange(0, (n-size +1 ) + (n-size)*n)
        while num in avoid:
            num = random.randrange(0, (n - size+ 1) + (n - size) * n)
            #print("num= ", num)
        # add top suburban group and also update avoid
        for k in range(rings):
            for l in range(size):
                tosub = k*n + num + l
                # print("to sub is ", tosub)
                precmap[tosub] = 1
                avoid.add(tosub)
                if i == 0:
                    for m in range(1, size):
                        toavoid = tosub - m*n
                        if toavoid >= 0:
                            avoid.add(toavoid)

        # add left suburban group and also update avoid
        num = num + rings*n
        bottomNum = num + n * (size-2*rings)
        for o in range(rings):
            for p in range(size - 2*rings):
                tosub = p * n + num + o
                # print("to sub is ", tosub)
                precmap[tosub] = 1
                avoid.add(tosub)
                if o == 0:
                    for q in range(1, size):
                        toavoid = tosub - q
                        if toavoid >= 0:
                            avoid.add(toavoid)
        # add urban
        num = num + rings
        for r in range(size-2*rings):
            for s in range(size-2*rings):
                tourban = r * n + num + s
                # print("to urban is ", tourban)
                precmap[tourban] = 2
                avoid.add(tourban)

        # add right suburban group
        num = num + (size-2*rings)
        for t in range(rings):
            for u in range(size - 2*rings):
                # print("to sub is ", tosub)
                tosub = u * n + num + t
                precmap[tosub] = 1
                avoid.add(tosub)

        # add bottom suburban group
        num = bottomNum
        for v in range(rings):
            for w in range(size):
                tosub = v*n + num + w
                # print ("to sub bottom is ", tosub)
                precmap[tosub] = 1
                avoid.add(tosub)

    return (precmap,avoid)

"Cuts up a single list of precincts into districts"

def districtMaker(precmap, districts, precincts):
    statemap = [[0 for x in range(precincts)] for x in range(districts)]
    start = 0
    for i in range(districts):
        if (i == districts - 1):
            statemap[i] = precmap[start:]
        else:
            statemap[i] = precmap[start:start + precincts]
            start += precincts
    return statemap;

"Generates packed maps for NC"

def packing(districts, precincts):
    statemap = [[0 for x in range(precincts)] for x in range(districts)]
    for i in range(7):
        for j in range(precincts):                 # create city districts
            num = random.randrange(0, 36)
            if (j < 64):
                statemap[i][j] = 2  # mark as urban
            elif (num < 18):
                statemap[i][j] = 1  # mark as suburban
            else:
                statemap[i][j] = 0  # mark as rural
    for i in range(7,13):
        for j in range(precincts):
            num = random.randrange(0, 100)
            if (num < 34):
                statemap[i][j] = 1  # mark as suburban
            else:
                statemap[i][j] = 0  # mark as rural
    return statemap

"Shuffles a given statemap, typically a packed map"

def unpacking(packed):
    # statemap = [[0 for x in range(len(packed[0]))] for x in range(len(packed))]
    unpack = packed[0]
    for arr in packed[1:]:       # combine all the precincts
        unpack += arr
    unpack = np.random.permutation(unpack)   # randomize
    statemap = [unpack[x:x + 100] for x in range(0, len(unpack), 100)]
    return statemap

"Generates voting results for a given map and state"

def voting(map):
    percentages = []
    for i in range(len(map)):
        total = 0
        for j in range(len(map[i])):

            if (map[i][j] == 2): # urban
                total += .58
            elif (map[i][j] == 1): # suburban
                total += .42
            else:                   # rural
                total += .4
        percentage = total/len(map[i])
        percentages.append(percentage)

    return percentages

"Fills a data list that can later be used to generate " \
"various charts. Also prints any desired output"

def output():
    data = []
    for k in range(10000): # number of simulations we want to do
        # ans = packing(13, 100)
        # ans = unpacking(ans)
        ans = setUp(13,100)
        # precincts = 1296
        # (precmap, avoid) = droppingCities2(precincts, 7, 10, 1)
        # (precmap, avoid) = droppingCities2(precincts, 3, 14, 3)
        precmap =[]
        # initmap = torusMap.makeNCMap()
        # initmap = torusMap.makePennMap()
        # initmap = torusMap.makeIllMap()
        # ans = unpackingTorus(initmap, 17)
        #ans = setUp(13, 100) # number of districts and precincts
        #ans = droppingCities(13, 16, 6)
        # for i in range(len(ans)):
        #     print(ans[i])
        perc = voting(ans)
        perc = sorted(perc)
        for i in range(len(perc)):
            data.append([perc[i],i+1])
        #print(perc)
    return data


if __name__ == '__main__':


    data = output() # prints output and fills data
    print (data)

