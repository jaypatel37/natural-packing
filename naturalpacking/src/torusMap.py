"Creates torus maps with various # of districts for NC, Pennsylvania, and Illinois."\
"Performs simulation on a created map by moving where the bottom right corner is after each run"

__author__ = "Jay Patel"

import numpy as np

"Creates mock NC map that we designed." \
"Each precinct (index) has three values." \
"First value: 0 for rural, 1 for suburban, and 2" \
"for urban. The second value is row number and the" \
"third value is column number"

def makeNCMap():
    statemap = []
    statemap.append([0,0,0])
    statemap.append([0,0,1])
    statemap.append([0,0,2])
    statemap.append([0,0,3])
    statemap.append([0, 0, 4])
    statemap.append([1, 0, 5])
    statemap.append([2, 0, 6])
    statemap.append([2, 0, 7])
    statemap.append([2, 0, 8])
    statemap.append([1, 0, 9])
    statemap.append([2, 0, 10])
    statemap.append([2, 0, 11])
    statemap.append([2, 0, 12])
    statemap.append([1, 0, 13])
    statemap.append([2, 0, 14])
    statemap.append([2, 0, 15])
    statemap.append([2, 0, 16])
    statemap.append([2, 0, 17])
    statemap.append([2, 0, 18])
    statemap.append([1, 0, 19])
    statemap.append([0, 0, 20])
    statemap.append([0, 0, 21])
    statemap.append([0, 0, 22])
    statemap.append([0, 0, 23])

    statemap.append([0, 1, 0])
    statemap.append([0, 1, 1])
    statemap.append([0, 1, 2])
    statemap.append([0, 1, 3])
    statemap.append([0, 1, 4])
    statemap.append([1, 1, 5])
    statemap.append([2, 1, 6])
    statemap.append([2, 1, 7])
    statemap.append([2, 1, 8])
    statemap.append([1, 1, 9])
    statemap.append([2, 1, 10])
    statemap.append([2, 1, 11])
    statemap.append([2, 1, 12])
    statemap.append([1, 1, 13])
    statemap.append([2, 1, 14])
    statemap.append([2, 1, 15])
    statemap.append([2, 1, 16])
    statemap.append([2, 1, 17])
    statemap.append([2, 1, 18])
    statemap.append([1, 1, 19])
    statemap.append([0, 1, 20])
    statemap.append([0, 1, 21])
    statemap.append([0, 1, 22])
    statemap.append([0, 1, 23])

    statemap.append([0, 2, 0])
    statemap.append([0, 2, 1])
    statemap.append([0, 2, 2])
    statemap.append([0, 2, 3])
    statemap.append([0, 2, 4])
    statemap.append([1, 2, 5])
    statemap.append([2, 2, 6])
    statemap.append([2, 2, 7])
    statemap.append([2, 2, 8])
    statemap.append([1, 2, 9])
    statemap.append([2, 2, 10])
    statemap.append([2, 2, 11])
    statemap.append([2, 2, 12])
    statemap.append([1, 2, 13])
    statemap.append([2, 2, 14])
    statemap.append([2, 2, 15])
    statemap.append([2, 2, 16])
    statemap.append([2, 2, 17])
    statemap.append([2, 2, 18])
    statemap.append([1, 2, 19])
    statemap.append([0, 2, 20])
    statemap.append([0, 2, 21])
    statemap.append([0, 2, 22])
    statemap.append([0, 2, 23])

    statemap.append([1, 3, 0])
    statemap.append([1, 3, 1])
    statemap.append([1, 3, 2])
    statemap.append([1, 3, 3])
    statemap.append([1, 3, 4])
    statemap.append([1, 3, 5])
    statemap.append([2, 3, 6])
    statemap.append([2, 3, 7])
    statemap.append([2, 3, 8])
    statemap.append([1, 3, 9])
    statemap.append([2, 3, 10])
    statemap.append([2, 3, 11])
    statemap.append([2, 3, 12])
    statemap.append([1, 3, 13])
    statemap.append([2, 3, 14])
    statemap.append([2, 3, 15])
    statemap.append([2, 3, 16])
    statemap.append([2, 3, 17])
    statemap.append([2, 3, 18])
    statemap.append([1, 3, 19])
    statemap.append([0, 3, 20])
    statemap.append([0, 3, 21])
    statemap.append([0, 3, 22])
    statemap.append([0, 3, 23])

    statemap.append([2, 4, 0])
    statemap.append([2, 4, 1])
    statemap.append([2, 4, 2])
    statemap.append([2, 4, 3])
    statemap.append([1, 4, 4])
    statemap.append([1, 4, 5])
    statemap.append([1, 4, 6])
    statemap.append([1, 4, 7])
    statemap.append([1, 4, 8])
    statemap.append([1, 4, 9])
    statemap.append([1, 4, 10])
    statemap.append([1, 4, 11])
    statemap.append([1, 4, 12])
    statemap.append([1, 4, 13])
    statemap.append([2, 4, 14])
    statemap.append([2, 4, 15])
    statemap.append([2, 4, 16])
    statemap.append([2, 4, 17])
    statemap.append([2, 4, 18])
    statemap.append([1, 4, 19])
    statemap.append([0, 4, 20])
    statemap.append([0, 4, 21])
    statemap.append([0, 4, 22])
    statemap.append([0, 4, 23])

    statemap.append([2, 5, 0])
    statemap.append([2, 5, 1])
    statemap.append([2, 5, 2])
    statemap.append([2, 5, 3])
    statemap.append([1, 5, 4])
    statemap.append([0, 5, 5])
    statemap.append([0, 5, 6])
    statemap.append([0, 5, 7])
    statemap.append([0, 5, 8])
    statemap.append([0, 5, 9])
    statemap.append([0, 5, 10])
    statemap.append([0, 5, 11])
    statemap.append([0, 5, 12])
    statemap.append([1, 5, 13])
    statemap.append([2, 5, 14])
    statemap.append([2, 5, 15])
    statemap.append([2, 5, 16])
    statemap.append([2, 5, 17])
    statemap.append([2, 5, 18])
    statemap.append([1, 5, 19])
    statemap.append([0, 5, 20])
    statemap.append([0, 5, 21])
    statemap.append([0, 5, 22])
    statemap.append([0, 5, 23])

    statemap.append([2, 6, 0])
    statemap.append([2, 6, 1])
    statemap.append([2, 6, 2])
    statemap.append([2, 6, 3])
    statemap.append([1, 6, 4])
    statemap.append([0, 6, 5])
    statemap.append([0, 6, 6])
    statemap.append([0, 6, 7])
    statemap.append([0, 6, 8])
    statemap.append([0, 6, 9])
    statemap.append([0, 6, 10])
    statemap.append([0, 6, 11])
    statemap.append([0, 6, 12])
    statemap.append([1, 6, 13])
    statemap.append([1, 6, 14])
    statemap.append([1, 6, 15])
    statemap.append([1, 6, 16])
    statemap.append([1, 6, 17])
    statemap.append([1, 6, 18])
    statemap.append([1, 6, 19])
    statemap.append([0, 6, 20])
    statemap.append([0, 6, 21])
    statemap.append([0, 6, 22])
    statemap.append([0, 6, 23])

    statemap.append((2, 7, 0))
    statemap.append((2, 7, 1))
    statemap.append((2, 7, 2))
    statemap.append((2, 7, 3))
    statemap.append((1, 7, 4))
    statemap.append((1, 7, 5))
    statemap.append((1, 7, 6))
    statemap.append((1, 7, 7))
    statemap.append((1, 7, 8))
    statemap.append((1, 7, 9))
    statemap.append((0, 7, 10))
    statemap.append((0, 7, 11))
    statemap.append((0, 7, 12))
    statemap.append((0, 7, 13))
    statemap.append((0, 7, 14))
    statemap.append((0, 7, 15))
    statemap.append((0, 7, 16))
    statemap.append((0, 7, 17))
    statemap.append((0, 7, 18))
    statemap.append((0, 7, 19))
    statemap.append((0, 7, 20))
    statemap.append((0, 7, 21))
    statemap.append((0, 7, 22))
    statemap.append((0, 7, 23))

    statemap.append((1, 8, 0))
    statemap.append((1, 8, 1))
    statemap.append((1, 8, 2))
    statemap.append((1, 8, 3))
    statemap.append((1, 8, 4))
    statemap.append((2, 8, 5))
    statemap.append((2, 8, 6))
    statemap.append((2, 8, 7))
    statemap.append((2, 8, 8))
    statemap.append((1, 8, 9))
    statemap.append((0, 8, 10))
    statemap.append((0, 8, 11))
    statemap.append((0, 8, 12))
    statemap.append((0, 8, 13))
    statemap.append((0, 8, 14))
    statemap.append((0, 8, 15))
    statemap.append((0, 8, 16))
    statemap.append((1, 8, 17))
    statemap.append((1, 8, 18))
    statemap.append((1, 8, 19))
    statemap.append((1, 8, 20))
    statemap.append((1, 8, 21))
    statemap.append((1, 8, 22))
    statemap.append((1, 8, 23))

    statemap.append((0, 9, 0))
    statemap.append((0, 9, 1))
    statemap.append((0, 9, 2))
    statemap.append((0, 9, 3))
    statemap.append((1, 9, 4))
    statemap.append((2, 9, 5))
    statemap.append((2, 9, 6))
    statemap.append((2, 9, 7))
    statemap.append((2, 9, 8))
    statemap.append((1, 9, 9))
    statemap.append((0, 9, 10))
    statemap.append((0, 9, 11))
    statemap.append((0, 9, 12))
    statemap.append((0, 9, 13))
    statemap.append((0, 9, 14))
    statemap.append((0, 9, 15))
    statemap.append((0, 9, 16))
    statemap.append((1, 9, 17))
    statemap.append((1, 9, 18))
    statemap.append((2, 9, 19))
    statemap.append((2, 9, 20))
    statemap.append((2, 9, 21))
    statemap.append((2, 9, 22))
    statemap.append((2, 9, 23))

    statemap.append((0, 10, 0))
    statemap.append((0, 10, 1))
    statemap.append((0, 10, 2))
    statemap.append((0, 10, 3))
    statemap.append((1, 10, 4))
    statemap.append((2, 10, 5))
    statemap.append((2, 10, 6))
    statemap.append((2, 10, 7))
    statemap.append((2, 10, 8))
    statemap.append((1, 10, 9))
    statemap.append((0, 10, 10))
    statemap.append((0, 10, 11))
    statemap.append((0, 10, 12))
    statemap.append((0, 10, 13))
    statemap.append((0, 10, 14))
    statemap.append((0, 10, 15))
    statemap.append((0, 10, 16))
    statemap.append((1, 10, 17))
    statemap.append((1, 10, 18))
    statemap.append((2, 10, 19))
    statemap.append((2, 10, 20))
    statemap.append((2, 10, 21))
    statemap.append((2, 10, 22))
    statemap.append((2, 10, 23))

    statemap.append((0, 11, 0))
    statemap.append((0, 11, 1))
    statemap.append((0, 11, 2))
    statemap.append((0, 11, 3))
    statemap.append((1, 11, 4))
    statemap.append((2, 11, 5))
    statemap.append((2, 11, 6))
    statemap.append((2, 11, 7))
    statemap.append((2, 11, 8))
    statemap.append((1, 11, 9))
    statemap.append((0, 11, 10))
    statemap.append((0, 11, 11))
    statemap.append((0, 11, 12))
    statemap.append((0, 11, 13))
    statemap.append((0, 11, 14))
    statemap.append((0, 11, 15))
    statemap.append((0, 11, 16))
    statemap.append((1, 11, 17))
    statemap.append((1, 11, 18))
    statemap.append((2, 11, 19))
    statemap.append((2, 11, 20))
    statemap.append((2, 11, 21))
    statemap.append((2, 11, 22))
    statemap.append((2, 11, 23))

    statemap.append((0, 12, 0))
    statemap.append((0, 12, 1))
    statemap.append((0, 12, 2))
    statemap.append((0, 12, 3))
    statemap.append((1, 12, 4))
    statemap.append((2, 12, 5))
    statemap.append((2, 12, 6))
    statemap.append((2, 12, 7))
    statemap.append((2, 12, 8))
    statemap.append((1, 12, 9))
    statemap.append((0, 12, 10))
    statemap.append((0, 12, 11))
    statemap.append((0, 12, 12))
    statemap.append((0, 12, 13))
    statemap.append((0, 12, 14))
    statemap.append((0, 12, 15))
    statemap.append((0, 12, 16))
    statemap.append((1, 12, 17))
    statemap.append((1, 12, 18))
    statemap.append((2, 12, 19))
    statemap.append((2, 12, 20))
    statemap.append((2, 12, 21))
    statemap.append((2, 12, 22))
    statemap.append((2, 12, 23))

    statemap.append((0, 13, 0))
    statemap.append((0, 13, 1))
    statemap.append((0, 13, 2))
    statemap.append((0, 13, 3))
    statemap.append((1, 13, 4))
    statemap.append((2, 13, 5))
    statemap.append((2, 13, 6))
    statemap.append((2, 13, 7))
    statemap.append((2, 13, 8))
    statemap.append((1, 13, 9))
    statemap.append((0, 13, 10))
    statemap.append((0, 13, 11))
    statemap.append((0, 13, 12))
    statemap.append((0, 13, 13))
    statemap.append((0, 13, 14))
    statemap.append((0, 13, 15))
    statemap.append((0, 13, 16))
    statemap.append((1, 13, 17))
    statemap.append((1, 13, 18))
    statemap.append((2, 13, 19))
    statemap.append((2, 13, 20))
    statemap.append((2, 13, 21))
    statemap.append((2, 13, 22))
    statemap.append((2, 13, 23))

    statemap.append((0, 14, 0))
    statemap.append((0, 14, 1))
    statemap.append((0, 14, 2))
    statemap.append((0, 14, 3))
    statemap.append((1, 14, 4))
    statemap.append((2, 14, 5))
    statemap.append((2, 14, 6))
    statemap.append((2, 14, 7))
    statemap.append((2, 14, 8))
    statemap.append((1, 14, 9))
    statemap.append((0, 14, 10))
    statemap.append((0, 14, 11))
    statemap.append((0, 14, 12))
    statemap.append((0, 14, 13))
    statemap.append((0, 14, 14))
    statemap.append((0, 14, 15))
    statemap.append((0, 14, 16))
    statemap.append((1, 14, 17))
    statemap.append((1, 14, 18))
    statemap.append((2, 14, 19))
    statemap.append((2, 14, 20))
    statemap.append((2, 14, 21))
    statemap.append((2, 14, 22))
    statemap.append((2, 14, 23))

    statemap.append((0, 15, 0))
    statemap.append((0, 15, 1))
    statemap.append((0, 15, 2))
    statemap.append((0, 15, 3))
    statemap.append((1, 15, 4))
    statemap.append((1, 15, 5))
    statemap.append((1, 15, 6))
    statemap.append((1, 15, 7))
    statemap.append((1, 15, 8))
    statemap.append((1, 15, 9))
    statemap.append((0, 15, 10))
    statemap.append((0, 15, 11))
    statemap.append((0, 15, 12))
    statemap.append((0, 15, 13))
    statemap.append((0, 15, 14))
    statemap.append((0, 15, 15))
    statemap.append((0, 15, 16))
    statemap.append((1, 15, 17))
    statemap.append((1, 15, 18))
    statemap.append((2, 15, 19))
    statemap.append((2, 15, 20))
    statemap.append((2, 15, 21))
    statemap.append((2, 15, 22))
    statemap.append((2, 15, 23))

    #this for loop is here because I accidentally made some entries tuples
    #instead of lists and they all need to be lists so that they are mutable
    for i in range(len(statemap)):
        item = statemap[i]
        replace = []
        replace.append(item[0])
        replace.append(item[1])
        replace.append(item[2])
        statemap[i] = replace
    return statemap

"Creates mock Pennsylvania map that we designed."
"Each precinct (index) has three values." \
"First value: 0 for rural, 1 for suburban, and 2" \
"for urban. The second value is row number and the" \
"third value is column number"

def makePennMap():
    statemap = []
    statemap.append((0, 0, 0))
    statemap.append((0, 0, 1))
    statemap.append((0, 0, 2))
    statemap.append((0, 0, 3))
    statemap.append((0, 0, 4))
    statemap.append((0, 0, 5))
    statemap.append((0, 0, 6))
    statemap.append((0, 0, 7))
    statemap.append((0, 0, 8))
    statemap.append((0, 0, 9))
    statemap.append((0, 0, 10))
    statemap.append((0, 0, 11))
    statemap.append((0, 0, 12))
    statemap.append((0, 0, 13))
    statemap.append((0, 0, 14))
    statemap.append((0, 0, 15))

    statemap.append((0, 1, 0))
    statemap.append((0, 1, 1))
    statemap.append((0, 1, 2))
    statemap.append((0, 1, 3))
    statemap.append((0, 1, 4))
    statemap.append((0, 1, 5))
    statemap.append((0, 1, 6))
    statemap.append((0, 1, 7))
    statemap.append((0, 1, 8))
    statemap.append((0, 1, 9))
    statemap.append((0, 1, 10))
    statemap.append((0, 1, 11))
    statemap.append((0, 1, 12))
    statemap.append((0, 1, 13))
    statemap.append((0, 1, 14))
    statemap.append((0, 1, 15))

    statemap.append((0, 2, 0))
    statemap.append((0, 2, 1))
    statemap.append((0, 2, 2))
    statemap.append((0, 2, 3))
    statemap.append((0, 2, 4))
    statemap.append((0, 2, 5))
    statemap.append((0, 2, 6))
    statemap.append((0, 2, 7))
    statemap.append((0, 2, 8))
    statemap.append((0, 2, 9))
    statemap.append((0, 2, 10))
    statemap.append((0, 2, 11))
    statemap.append((0, 2, 12))
    statemap.append((0, 2, 13))
    statemap.append((0, 2, 14))
    statemap.append((0, 2, 15))

    statemap.append((0, 3, 0))
    statemap.append((0, 3, 1))
    statemap.append((0, 3, 2))
    statemap.append((0, 3, 3))
    statemap.append((0, 3, 4))
    statemap.append((0, 3, 5))
    statemap.append((0, 3, 6))
    statemap.append((0, 3, 7))
    statemap.append((0, 3, 8))
    statemap.append((0, 3, 9))
    statemap.append((0, 3, 10))
    statemap.append((0, 3, 11))
    statemap.append((0, 3, 12))
    statemap.append((0, 3, 13))
    statemap.append((0, 3, 14))
    statemap.append((0, 3, 15))

    statemap.append((1, 4, 0))
    statemap.append((1, 4, 1))
    statemap.append((1, 4, 2))
    statemap.append((1, 4, 3))
    statemap.append((1, 4, 4))
    statemap.append((1, 4, 5))
    statemap.append((1, 4, 6))
    statemap.append((1, 4, 7))
    statemap.append((1, 4, 8))
    statemap.append((1, 4, 9))
    statemap.append((1, 4, 10))
    statemap.append((1, 4, 11))
    statemap.append((1, 4, 12))
    statemap.append((1, 4, 13))
    statemap.append((1, 4, 14))
    statemap.append((1, 4, 15))

    statemap.append((1, 5, 0))
    statemap.append((1, 5, 1))
    statemap.append((1, 5, 2))
    statemap.append((1, 5, 3))
    statemap.append((1, 5, 4))
    statemap.append((1, 5, 5))
    statemap.append((1, 5, 6))
    statemap.append((1, 5, 7))
    statemap.append((1, 5, 8))
    statemap.append((1, 5, 9))
    statemap.append((1, 5, 10))
    statemap.append((1, 5, 11))
    statemap.append((1, 5, 12))
    statemap.append((1, 5, 13))
    statemap.append((1, 5, 14))
    statemap.append((1, 5, 15))

    statemap.append((1, 6, 0))
    statemap.append((1, 6, 1))
    statemap.append((1, 6, 2))
    statemap.append((1, 6, 3))
    statemap.append((1, 6, 4))
    statemap.append((1, 6, 5))
    statemap.append((1, 6, 6))
    statemap.append((1, 6, 7))
    statemap.append((1, 6, 8))
    statemap.append((2, 6, 9))
    statemap.append((2, 6, 10))
    statemap.append((2, 6, 11))
    statemap.append((2, 6, 12))
    statemap.append((2, 6, 13))
    statemap.append((2, 6, 14))
    statemap.append((2, 6, 15))

    statemap.append((1, 7, 0))
    statemap.append((2, 7, 1))
    statemap.append((2, 7, 2))
    statemap.append((2, 7, 3))
    statemap.append((2, 7, 4))
    statemap.append((1, 7, 5))
    statemap.append((1, 7, 6))
    statemap.append((1, 7, 7))
    statemap.append((1, 7, 8))
    statemap.append((2, 7, 9))
    statemap.append((2, 7, 10))
    statemap.append((2, 7, 11))
    statemap.append((2, 7, 12))
    statemap.append((2, 7, 13))
    statemap.append((2, 7, 14))
    statemap.append((2, 7, 15))

    statemap.append((1, 8, 0))
    statemap.append((2, 8, 1))
    statemap.append((2, 8, 2))
    statemap.append((2, 8, 3))
    statemap.append((2, 8, 4))
    statemap.append((1, 8, 5))
    statemap.append((1, 8, 6))
    statemap.append((1, 8, 7))
    statemap.append((1, 8, 8))
    statemap.append((2, 8, 9))
    statemap.append((2, 8, 10))
    statemap.append((2, 8, 11))
    statemap.append((2, 8, 12))
    statemap.append((2, 8, 13))
    statemap.append((2, 8, 14))
    statemap.append((2, 8, 15))

    statemap.append((1, 9, 0))
    statemap.append((2, 9, 1))
    statemap.append((2, 9, 2))
    statemap.append((2, 9, 3))
    statemap.append((2, 9, 4))
    statemap.append((1, 9, 5))
    statemap.append((1, 9, 6))
    statemap.append((1, 9, 7))
    statemap.append((1, 9, 8))
    statemap.append((2, 9, 9))
    statemap.append((2, 9, 10))
    statemap.append((2, 9, 11))
    statemap.append((2, 9, 12))
    statemap.append((2, 9, 13))
    statemap.append((2, 9, 14))
    statemap.append((2, 9, 15))

    statemap.append((1, 10, 0))
    statemap.append((2, 10, 1))
    statemap.append((2, 10, 2))
    statemap.append((2, 10, 3))
    statemap.append((2, 10, 4))
    statemap.append((1, 10, 5))
    statemap.append((1, 10, 6))
    statemap.append((1, 10, 7))
    statemap.append((1, 10, 8))
    statemap.append((2, 10, 9))
    statemap.append((2, 10, 10))
    statemap.append((2, 10, 11))
    statemap.append((2, 10, 12))
    statemap.append((2, 10, 13))
    statemap.append((2, 10, 14))
    statemap.append((2, 10, 15))

    statemap.append((1, 11, 0))
    statemap.append((1, 11, 1))
    statemap.append((1, 11, 2))
    statemap.append((1, 11, 3))
    statemap.append((1, 11, 4))
    statemap.append((1, 11, 5))
    statemap.append((1, 11, 6))
    statemap.append((1, 11, 7))
    statemap.append((1, 11, 8))
    statemap.append((2, 11, 9))
    statemap.append((2, 11, 10))
    statemap.append((2, 11, 11))
    statemap.append((2, 11, 12))
    statemap.append((2, 11, 13))
    statemap.append((2, 11, 14))
    statemap.append((2, 11, 15))

    statemap.append((1, 12, 0))
    statemap.append((1, 12, 1))
    statemap.append((1, 12, 2))
    statemap.append((1, 12, 3))
    statemap.append((1, 12, 4))
    statemap.append((1, 12, 5))
    statemap.append((1, 12, 6))
    statemap.append((1, 12, 7))
    statemap.append((1, 12, 8))
    statemap.append((2, 12, 9))
    statemap.append((2, 12, 10))
    statemap.append((2, 12, 11))
    statemap.append((2, 12, 12))
    statemap.append((2, 12, 13))
    statemap.append((2, 12, 14))
    statemap.append((2, 12, 15))

    statemap.append((1, 13, 0))
    statemap.append((1, 13, 1))
    statemap.append((1, 13, 2))
    statemap.append((1, 13, 3))
    statemap.append((1, 13, 4))
    statemap.append((1, 13, 5))
    statemap.append((1, 13, 6))
    statemap.append((1, 13, 7))
    statemap.append((1, 13, 8))
    statemap.append((2, 13, 9))
    statemap.append((2, 13, 10))
    statemap.append((2, 13, 11))
    statemap.append((2, 13, 12))
    statemap.append((2, 13, 13))
    statemap.append((2, 13, 14))
    statemap.append((2, 13, 15))

    statemap.append((0, 14, 0))
    statemap.append((0, 14, 1))
    statemap.append((0, 14, 2))
    statemap.append((0, 14, 3))
    statemap.append((0, 14, 4))
    statemap.append((0, 14, 5))
    statemap.append((1, 14, 6))
    statemap.append((1, 14, 7))
    statemap.append((1, 14, 8))
    statemap.append((2, 14, 9))
    statemap.append((2, 14, 10))
    statemap.append((2, 14, 11))
    statemap.append((2, 14, 12))
    statemap.append((2, 14, 13))
    statemap.append((2, 14, 14))
    statemap.append((2, 14, 15))

    statemap.append((0, 15, 0))
    statemap.append((0, 15, 1))
    statemap.append((0, 15, 2))
    statemap.append((0, 15, 3))
    statemap.append((0, 15, 4))
    statemap.append((0, 15, 5))
    statemap.append((1, 15, 6))
    statemap.append((1, 15, 7))
    statemap.append((1, 15, 8))
    statemap.append((2, 15, 9))
    statemap.append((2, 15, 10))
    statemap.append((2, 15, 11))
    statemap.append((2, 15, 12))
    statemap.append((2, 15, 13))
    statemap.append((2, 15, 14))
    statemap.append((2, 15, 15))

    # this for loop is here because I accidentally made some entries tuples
    # instead of lists and they all need to be lists so that they are mutable
    for i in range(len(statemap)):
        item = statemap[i]
        replace = []
        replace.append(item[0])
        replace.append(item[1])
        replace.append(item[2])
        statemap[i] = replace
    return statemap

"Creates mock Illinois map that we designed."
"Each precinct (index) has three values." \
"First value: 0 for rural, 1 for suburban, and 2" \
"for urban. The second value is row number and the" \
"third value is column number"

def makeIllMap():
    statemap = []
    for i in range(12):
        statemap.append([1, i, 0])
        statemap.append([2, i, 1])
        statemap.append([2, i, 2])
        statemap.append([2, i, 3])
        statemap.append([2, i, 4])
        statemap.append([2, i, 5])
        statemap.append([2, i, 6])
        statemap.append([2, i, 7])

    for j in range(12,16):
        statemap.append([1, j, 0])
        statemap.append([1, j, 1])
        statemap.append([1, j, 2])
        statemap.append([1, j, 3])
        statemap.append([1, j, 4])
        statemap.append([1, j, 5])
        statemap.append([1, j, 6])
        statemap.append([1, j, 7])

    for k in range(16,24):
        statemap.append([0, k, 0])
        statemap.append([0, k, 1])
        statemap.append([0, k, 2])
        statemap.append([0, k, 3])
        statemap.append([0, k, 4])
        statemap.append([0, k, 5])
        statemap.append([0, k, 6])
        statemap.append([0, k, 7])

    return statemap
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

"Generates voting results for a given map and state"

def votingCalc(districts, state):
    percentages = []
    for i in range(len(districts)):
        total = 0
        for j in range(len(districts[i])):
            #  -- NC --
            if state == "NC":
                if (districts[i][j][0] == 2): # urban
                    total += .58
                elif (districts[i][j][0] == 1): # suburban
                    total += .42
                else:                   # rural
                    total += .40
            #  -- Penn --
            if state == "Penn":
                if (districts[i][j][0] == 2): # urban
                    total += .65
                elif (districts[i][j][0] == 1): # suburban
                    total += .55
                else:                   # rural
                    total += .43
            #  -- Illinois --
            if state == "Ill":
                if (districts[i][j][0] == 2): # urban
                    total += .68
                elif (districts[i][j][0] == 1): # suburban
                    total += .58
                else:                   # rural
                    total += .40

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

def simulate(statemap, distNum, dir, cols, rows):
    data = []
    districts = splitIntoDistricts(statemap, distNum, dir, cols, rows)
    for i in range(rows +1):    # rows is last row index
        for j in range(cols + 1):  # cols is last column index
            perc = votingCalc(districts, "NC")
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
    statemap = makeNCMap()
    # statemap = makePennMap()
    # statemap = makeIllMap()
    # print(statemap)
    data = simulate(statemap, 2, 1, 23, 15)
    print(data)

