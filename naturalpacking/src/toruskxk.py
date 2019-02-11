'''
Created on Jan 30, 2019

@author: ellavanengen
'''
import numpy as np
import random



def makeKbyKMap(k, dist,precinctsPerDistrict):
    statemap = [[0 for x in range(precinctsPerDistrict)] for x in range(dist)]
    for i in range(dist):
        count=0
        for j in range (k**2):
            num = random.randrange(0,100)
            if (num < 40):
                statemap[i][count*precinctsPerDistrict//k**2] = 0 #mark as republican
                for p in range((precinctsPerDistrict//k**2)-1):
                    statemap[i][(count*precinctsPerDistrict//k**2)+(p+1)]=0
            else:
                statemap[i][count*precinctsPerDistrict//k**2] = 1 #mark as democratic
                for p in range((precinctsPerDistrict//(k**2))-1):
                    statemap[i][(count*precinctsPerDistrict//k**2)+(p+1)]=1
            count+=1

    return statemap

def KbyKVotingResults(statemap):
    percentages = []
    for i in range(len(statemap)):
        total=0
        for j in range(len(statemap[i])):
            # print("Prec:", len(statemap[i]))
            total+=statemap[i][j]
        print("total:", total)
        total=total/(len(statemap[i]))
        percentages.append(total)

    return percentages
    
"Splits a given torus map into a certain number of districts." \
"For some numbers, the map can be split vertically or horizontally"
# make dir 0 for vertical splits and 1 for horizontal splits

def splitIntoDistricts(torusmap, distNum, dir, cols, rows):
    districts = []
    if distNum == 1:
        toAdd1 = []
        for item in torusmap:
            toAdd1.append(item)
        districts.append(toAdd1)
    if distNum == 2 and dir == 0:
        toAdd1 = []
        toAdd2 = []
        split = cols/2
        for item in torusmap:
            if item[2] < split:
                toAdd1.append(item)
            else:
                toAdd2.append(item)
        districts.append(toAdd1)
        districts.append(toAdd2)
    if distNum == 2 and dir == 1:
        toAdd1 = []
        toAdd2 = []
        split = cols/2
        for item in torusmap:
            if item[1] < split:
                toAdd1.append(item)
            else:
                toAdd2.append(item)
        districts.append(toAdd1)
        districts.append(toAdd2)
    if distNum == 4:
        toAdd1 = []
        toAdd2 = []
        toAdd3 = []
        toAdd4 = []
        splitVert = cols/2
        splitHor = rows/2
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
    if distNum == 8 and dir ==0:
        toAdd1 = []
        toAdd2 = []
        toAdd3 = []
        toAdd4 = []
        toAdd5 = []
        toAdd6 = []
        toAdd7 = []
        toAdd8 = []
        splitVert1 = cols/4
        splitVert2 = splitVert1 * 2
        splitVert3 = splitVert1 * 3
        splitHor = rows /2
        for item in torusmap:
            if item[2] < splitVert1 and item[1] < splitHor:
                toAdd1.append(item)
            elif item[2] < splitVert2 and item[1] < splitHor:
                toAdd2.append(item)
            elif item[2] < splitVert3 and item[1] < splitHor:
                toAdd3.append(item)
            elif item[2] > splitVert3 and item[1] < splitHor:
                toAdd4.append(item)
            elif item[2] < splitVert1 and item[1] > splitHor:
                toAdd5.append(item)
            elif item[2] < splitVert2 and item[1] > splitHor:
                toAdd6.append(item)
            elif item[2] < splitVert3 and item[1] > splitHor:
                toAdd7.append(item)
            elif item[2] > splitVert3 and item[1] > splitHor:
                toAdd8.append(item)
        districts.append(toAdd1)
        districts.append(toAdd2)
        districts.append(toAdd3)
        districts.append(toAdd4)
        districts.append(toAdd5)
        districts.append(toAdd6)
        districts.append(toAdd7)
        districts.append(toAdd8)

    if distNum == 8 and dir ==1:
        toAdd1 = []
        toAdd2 = []
        toAdd3 = []
        toAdd4 = []
        toAdd5 = []
        toAdd6 = []
        toAdd7 = []
        toAdd8 = []
        splitHor1 = rows/4
        splitHor2 = splitHor1 * 2
        splitHor3 = splitHor1 * 3
        splitVert = cols/2
        for item in torusmap:
            if item[1] < splitHor1 and item[2] < splitVert:
                toAdd1.append(item)
            elif item[1] < splitHor2 and item[2] < splitVert:
                toAdd2.append(item)
            elif item[1] < splitHor3 and item[2] < splitVert:
                toAdd3.append(item)
            elif item[1] > splitHor3 and item[2] < splitVert:
                toAdd4.append(item)
            elif item[1] < splitHor1 and item[2] > splitVert:
                toAdd5.append(item)
            elif item[1] < splitHor2 and item[2] > splitVert:
                toAdd6.append(item)
            elif item[1] < splitHor3 and item[2] > splitVert:
                toAdd7.append(item)
            elif item[1] > splitHor3 and item[2] > splitVert:
                toAdd8.append(item)
        districts.append(toAdd1)
        districts.append(toAdd2)
        districts.append(toAdd3)
        districts.append(toAdd4)
        districts.append(toAdd5)
        districts.append(toAdd6)
        districts.append(toAdd7)
        districts.append(toAdd8)

    if distNum == 12:
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
        splitVert1 = cols/6
        splitVert2 = splitVert1 * 2
        splitVert3 = splitVert1 * 3
        splitVert4 = splitVert1 * 4
        splitVert5 = splitVert1 * 5
        splitHor = rows / 2
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
            elif item[2] > splitVert5 and item[1] < splitHor:
                toAdd6.append(item)
            elif item[2] < splitVert1 and item[1] > splitHor:
                toAdd7.append(item)
            elif item[2] < splitVert2 and item[1] > splitHor:
                toAdd8.append(item)
            elif item[2] < splitVert3 and item[1] > splitHor:
                toAdd9.append(item)
            elif item[2] < splitVert4 and item[1] > splitHor:
                toAdd10.append(item)
            elif item[2] < splitVert5 and item[1] > splitHor:
                toAdd11.append(item)
            elif item[2] > splitVert5 and item[1] > splitHor:
                toAdd12.append(item)
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
        splitVert1 = cols /8
        splitVert2 = splitVert1 * 2
        splitVert3 = splitVert1 * 3
        splitVert4 = splitVert1 * 4
        splitVert5 = splitVert1 * 5
        splitVert6 = splitVert1 * 6
        splitVert7 = splitVert1 * 7
        splitHor = rows / 2
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

    if distNum == 24:
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
        toAdd17 = []
        toAdd18 = []
        toAdd19 = []
        toAdd20 = []
        toAdd21 = []
        toAdd22 = []
        toAdd23 = []
        toAdd24 = []
        splitVert1 = cols /6
        splitVert2 = splitVert1 * 2
        splitVert3 = splitVert1 * 3
        splitVert4 = splitVert1 * 4
        splitVert5 = splitVert1 * 5
        splitHor1 = rows /4
        splitHor2 = splitHor1 * 2
        splitHor3 = splitHor1 * 3
        for item in torusmap:
            if item[2] < splitVert1 and item[1] < splitHor1:
                toAdd1.append(item)
            elif item[2] < splitVert2 and item[1] < splitHor1:
                toAdd2.append(item)
            elif item[2] < splitVert3 and item[1] < splitHor1:
                toAdd3.append(item)
            elif item[2] < splitVert4 and item[1] < splitHor1:
                toAdd4.append(item)
            elif item[2] < splitVert5 and item[1] < splitHor1:
                toAdd5.append(item)
            elif item[2] > splitVert5 and item[1] < splitHor1:
                toAdd6.append(item)
            elif item[2] < splitVert1 and item[1] < splitHor2:
                toAdd7.append(item)
            elif item[2] < splitVert2 and item[1] < splitHor2:
                toAdd8.append(item)
            elif item[2] < splitVert3 and item[1] < splitHor2:
                toAdd9.append(item)
            elif item[2] < splitVert4 and item[1] < splitHor2:
                toAdd10.append(item)
            elif item[2] < splitVert5 and item[1] < splitHor2:
                toAdd11.append(item)
            elif item[2] > splitVert5 and item[1] < splitHor2:
                toAdd12.append(item)
            elif item[2] < splitVert1 and item[1] < splitHor3:
                toAdd13.append(item)
            elif item[2] < splitVert2 and item[1] < splitHor3:
                toAdd14.append(item)
            elif item[2] < splitVert3 and item[1] < splitHor3:
                toAdd15.append(item)
            elif item[2] < splitVert4 and item[1] < splitHor3:
                toAdd16.append(item)
            elif item[2] < splitVert5 and item[1] < splitHor3:
                toAdd17.append(item)
            elif item[2] > splitVert5 and item[1] < splitHor3:
                toAdd18.append(item)
            elif item[2] < splitVert1 and item[1] > splitHor3:
                toAdd19.append(item)
            elif item[2] < splitVert2 and item[1] > splitHor3:
                toAdd20.append(item)
            elif item[2] < splitVert3 and item[1] > splitHor3:
                toAdd21.append(item)
            elif item[2] < splitVert4 and item[1] > splitHor3:
                toAdd22.append(item)
            elif item[2] < splitVert5 and item[1] > splitHor3:
                toAdd23.append(item)
            elif item[2] > splitVert5 and item[1] > splitHor3:
                toAdd24.append(item)
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
        districts.append(toAdd17)
        districts.append(toAdd18)
        districts.append(toAdd19)
        districts.append(toAdd20)
        districts.append(toAdd21)
        districts.append(toAdd22)
        districts.append(toAdd23)
        districts.append(toAdd24)

    return districts


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

def simulate(statemap, distNum, dir, cols, rows):
    data = []
    districts = splitIntoDistricts(statemap, distNum, dir, cols, rows)
    for i in range(rows +1):    # rows is last row index
        for j in range(cols + 1):  # cols is last column index
            perc = KbyKVotingResults(statemap)
            perc = sorted(perc)
            for i in range(len(perc)):
                data.append([perc[i], i + 1])
            districts = columnShift(districts, cols)
            newstatemap = districtsToStateMap(districts)
            districts = splitIntoDistricts(newstatemap, distNum, dir, cols, rows)
        districts = rowShift(districts, rows)
        newstatemap2 = districtsToStateMap(districts)
        districts = splitIntoDistricts(newstatemap2, distNum, dir, cols, rows)
    return data


if __name__ == '__main__':
    statemap=makeKbyKMap(2, 9,64)
    print(statemap)
    print (KbyKVotingResults(statemap))
    data = simulate(statemap, 2, 1, 15, 23)
    print(data)
