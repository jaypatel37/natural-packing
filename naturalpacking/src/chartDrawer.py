"Where all charts are drawn using data created by the other programs in src"

__author__ = "Jay Patel"

import pandas as pd
import seaborn as sns
from src import natPacking
from src import readEnsembleNCHR
from src import torusMap
import matplotlib.pyplot as plt

"Creates boxplots"

def createBoxPlot(data):
    df = pd.DataFrame(data, columns=["Voting %", "From Maximum Rep. Vote to Maximum Dem. Vote"]) # construct the DataFrame
    box = sns.boxplot(x="From Maximum Rep. Vote to Maximum Dem. Vote", y="Voting %", data=df, showfliers=False)    # create the box plot
    plt.show()    # show the plot
    return df;

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

if __name__ == '__main__':

    data = natPacking.output()  # fills data
    df = createBoxPlot(data)

    # (avgs, counts) = readEnsembleNCHR.read("../data/MCMCElectionMargins_ALLNEW_USHOUSEOFREPRESENTATIVES_16_Sorted")
    # ansList = readEnsembleNCHR.createList(counts)
    # createNormalGraph(ansList)
    # data = readEnsembleNCHR.organizeForBarGraph(counts)
    # barGraph(data)

    # statemap = torusMap.makeNCMap()
    # statemap = torusMap.makePennMap()
    # statemap = torusMap.makeIllMap()
    # data = torusMap.simulate(statemap, 24, 0, 7, 23)
    # df = createBoxPlot(data)
    # print(df)                # left this here in case someone wants to see what the DataFrame looks like