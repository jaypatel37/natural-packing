'''
Created on Jan 30, 2019

@author: ellavanengen, jaypatel
'''
import numpy as np
import random
import math


"[value, row, column]"

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
                                statemap.append([0, row, column])
                            else:                       # assign as Democrat (1)
                                statemap.append([1, row, column])
    return statemap
    
"Splits a given torus map into a certain number of districts." \
"For some numbers, the map can be split vertically or horizontally"

def splitIntoDistricts(torusmap, distNum, maxColNum, maxRowNum):
    districts = []
    if distNum == 1:
        toAdd1 = []
        for item in torusmap:
            toAdd1.append(item)
        districts.append(toAdd1)

    if distNum == 4:
        toAdd1 = []
        toAdd2 = []
        toAdd3 = []
        toAdd4 = []
        splitVert = maxColNum/2
        splitHor = maxRowNum/2
        for item in torusmap:
            if item[2] < splitVert and item[1] < splitHor:
                toAdd1.append(item)
            elif item[2] > splitVert and item[1] < splitHor:
                toAdd2.append(item)
            elif item[2] < splitVert and item[1] > splitHor:
                toAdd3.append(item)
            else:
                toAdd4.append(item)
        districts.append(toAdd1)
        districts.append(toAdd2)
        districts.append(toAdd3)
        districts.append(toAdd4)

    if distNum == 16:
        toAdd1 = []
        toAdd2 = []
        toAdd3 = []
        toAdd4 = []
        toAdd5 = []
        toAdd6 = []
        toAdd7 = []
        toAdd8 = []
        toAdd9 = []
        toAdd10 = []
        toAdd11 = []
        toAdd12 = []
        toAdd13 = []
        toAdd14 = []
        toAdd15 = []
        toAdd16 = []
        splitVert1 = maxColNum /8
        splitVert2 = splitVert1 * 2
        splitVert3 = splitVert1 * 3
        splitVert4 = splitVert1 * 4
        splitVert5 = splitVert1 * 5
        splitVert6 = splitVert1 * 6
        splitVert7 = splitVert1 * 7
        splitHor = maxRowNum / 2
        for item in torusmap:
            if item[2] < splitVert1 and item[1] < splitHor:
                toAdd1.append(item)
            elif item[2] < splitVert2 and item[1] < splitHor:
                toAdd2.append(item)
            elif item[2] < splitVert3 and item[1] < splitHor:
                toAdd3.append(item)
            elif item[2] < splitVert4 and item[1] < splitHor:
                toAdd4.append(item)
            elif item[2] < splitVert5 and item[1] < splitHor:
                toAdd5.append(item)
            elif item[2] < splitVert6 and item[1] < splitHor:
                toAdd6.append(item)
            elif item[2] < splitVert7 and item[1] < splitHor:
                toAdd7.append(item)
            elif item[2] > splitVert7 and item[1] < splitHor:
                toAdd8.append(item)
            elif item[2] < splitVert1 and item[1] > splitHor:
                toAdd9.append(item)
            elif item[2] < splitVert2 and item[1] > splitHor:
                toAdd10.append(item)
            elif item[2] < splitVert3 and item[1] > splitHor:
                toAdd11.append(item)
            elif item[2] < splitVert4 and item[1] > splitHor:
                toAdd12.append(item)
            elif item[2] < splitVert5 and item[1] > splitHor:
                toAdd13.append(item)
            elif item[2] < splitVert6 and item[1] > splitHor:
                toAdd14.append(item)
            elif item[2] < splitVert7 and item[1] > splitHor:
                toAdd15.append(item)
            elif item[2] > splitVert7 and item[1] > splitHor:
                toAdd16.append(item)
        districts.append(toAdd1)
        districts.append(toAdd2)
        districts.append(toAdd3)
        districts.append(toAdd4)
        districts.append(toAdd5)
        districts.append(toAdd6)
        districts.append(toAdd7)
        districts.append(toAdd8)
        districts.append(toAdd9)
        districts.append(toAdd10)
        districts.append(toAdd11)
        districts.append(toAdd12)
        districts.append(toAdd13)
        districts.append(toAdd14)
        districts.append(toAdd15)
        districts.append(toAdd16)

    return districts

"Generates voting results for a given map"

def votingCalcKbyK(districts):
    percentages = []
    for i in range(len(districts)):
        total = 0
        for j in range(len(districts[i])):
            total += districts[i][j][0]
        percentage = total/len(districts[i])
        percentages.append(percentage)

    return percentages

"Shifts every column in the torus over to the right by 1." \
"The rightmost column becomes the leftmost column"

def columnShift(districts, vert):
    max = vert
    for dist in districts:
        for item in dist:
            if item[2] != max:
                item[2] +=1
            else:
                item[2] = 0
    return districts

"Shifts every row in the torus down by 1. The bottom row becomes" \
"the new top row"

def rowShift(districts, hor):
    max = hor
    for dist in districts:
        for item in dist:
            if item[1] != max:
                item[1] +=1
            else:
                item[1] = 0
    return districts

"Takes a list of list of districts (where each district is a " \
"list of precincts) and converts them to a traditional" \
"statemap: a single list of districts"

def districtsToStateMap(districts):
    stmap = []
    for dist in districts:
        for item in dist:
            stmap.append(item)
    return stmap

"Shuffles a torus map"

def unpackingTorus(torus, dist):
    unpack2 = []
    for item in torus:
        unpack2 += [item[0]]
    unpack2 = np.random.permutation(unpack2)  # randomize
    precnum = len(unpack2) / dist
    precnum = int(precnum)
    statemap = [unpack2[x:x + precnum] for x in range(0, len(unpack2), precnum)]
    return statemap

"Runs the simulation on the torus map. Returns a list of voting data" \
"that boxplots can be generated from"

def simulateKbyK(statemap, distNum, maxColNum, maxRowNum):
    data = []
    districts = splitIntoDistricts(statemap, distNum, maxColNum, maxRowNum)
    for i in range(maxRowNum +1):    # maxRowNum is last row index
        for j in range(maxColNum + 1):  # maxColNum is last column index
            votingPercentages = votingCalcKbyK(districts)
            votingPercentages = sorted(votingPercentages)
            for i in range(len(votingPercentages)):
                data.append([votingPercentages[i], i + 1])
            districts = columnShift(districts, maxColNum)
            newstatemap = districtsToStateMap(districts)
            districts = splitIntoDistricts(newstatemap, distNum, maxColNum, maxRowNum)
        districts = rowShift(districts, maxRowNum)
        newstatemap2 = districtsToStateMap(districts)
        districts = splitIntoDistricts(newstatemap2, distNum, maxColNum, maxRowNum)
    return data


if __name__ == '__main__':
    statemap=makeKbyKMap(4, 16,256)
    print(statemap)
    data = simulateKbyK(statemap, 16, 63, 63)
    print(data)
