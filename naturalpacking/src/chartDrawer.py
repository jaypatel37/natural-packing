"Where all charts are drawn using data created by the other programs in src"

__author__ = "Jay Patel"

import pandas as pd
import numpy as np
import seaborn as sns
from src import natPacking
from src import readEnsembleNCHR
from src import torusMap
from sklearn import linear_model
from src import toruskxk
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go

"Creates boxplots"

def createBoxPlot(data):
    df = pd.DataFrame(data, columns=["Voting %", "From Maximum Rep. Vote to Maximum Dem. Vote"]) # construct the DataFrame
    box = sns.boxplot(x="From Maximum Rep. Vote to Maximum Dem. Vote", y="Voting %", data=df, showfliers=False)    # create the box plot
    sns.set()
    plt.show()    # show the plot
    return df

def createViolinPlot(data):
    df = pd.DataFrame(data, columns=["Voting %", "From Maximum Rep. Vote to Maximum Dem. Vote"])  # construct the DataFrame
    violin = sns.violinplot(x="From Maximum Rep. Vote to Maximum Dem. Vote", y="Voting %", data=df)  # create the violin plot
    sns.set()
    plt.show()  # show the plot
    return df

"Creates normal graphs"

def createNormalGraph(data):
    # df = pd.DataFrame(data, columns=["Districts Won", "Amount"])
    # print(df)
    sns.distplot(data)
    plt.show()

"Creates bar graphs"

def barGraph(data):
    df = pd.DataFrame(data, columns=["% of Maps in Ensemble", "Number of Dem. Seats"])  # construct the DataFrame
    bar = sns.barplot(x="Number of Dem. Seats", y="% of Maps in Ensemble", data=df)
    plt.show()

def bestFit(data):
    df = pd.DataFrame(data, columns=["Voting %", "From Maximum Rep. Vote to Maximum Dem. Vote"])
    sns.lmplot(x="From Maximum Rep. Vote to Maximum Dem. Vote", y="Voting %",data=df)
    # regr = linear_model.LinearRegression()
    # X = df.x.values.reshape(-1,1)
    # y = df.y.values.reshape(-1,1)
    # regr.fit(X, y)
    # print(regr.intercept_)
    plt.show()
    return


def averageSeatShare(data, numdistricts):
    seatShare = []
    demcount = 0
    for i in range(len(data)):
        if data[i][0] > 0.5:
            demcount += 1
        # if data[i][0] == .5:
        #     demcount += .5
        if data[i][1] % numdistricts == 0:
            seatShare.append(demcount)
            demcount = 0

    return (sum(seatShare) / len(seatShare)) / numdistricts

if __name__ == '__main__':

    # data = natPacking.output()  # fills data
    # df = createBoxPlot(data)

    # (avgs, counts) = readEnsembleNCHR.read("../data/MCMCElectionMargins_ALLNEW_USHOUSEOFREPRESENTATIVES_16_Sorted")
    # ansList = readEnsembleNCHR.createList(counts)
    # createNormalGraph(ansList)
    # data = readEnsembleNCHR.organizeForBarGraph(counts)
    # barGraph(data)

    # statemap = torusMap.makeNCMap()
    # statemap = torusMap.makePennMap()
    # statemap = torusMap.makeIllMap()
    # statemap = toruskxk.makeKbyKMapSplitBlock(2, 16,16)
    data =[]
    for i in range(50):
        statemap = toruskxk.makeKbyKMap(8, 16, 256)
        tempdata = toruskxk.simulateKbyK(statemap, 16, 63, 63)
        data.extend(tempdata)
    print (data)
    # bestFit(data)
    print (averageSeatShare(data, 16))
    # data = torusMap.simulate(statemap, 24, 0, 7, 23)
    df = createViolinPlot(data)
    # print(df)                # left this here in case someone wants to see what the DataFrame looks like