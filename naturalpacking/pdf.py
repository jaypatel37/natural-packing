import scipy
import math
from scipy.stats import norm
from scipy.stats import binom
from scipy.special import comb
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.integrate as integrate
from scipy.stats import binom
import seaborn as sns
import random
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
import chartDrawer
import toruskxk
import torusMap

#UNIFORMLY DISTRIBUTED

##PLOT THE PDF
##
n = 16
p = .47
k = 256
data = []
for i in range(1,n+1):
	data_i = []
	for m in range(100): 
		b = random.random()
		cdf_z = lambda x: sum(comb(n,j) * (norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**j * (1-norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**(n-j) for j in range(i,n+1)) - b
		a = optimize.brentq(cdf_z,0,1)
		data_i.append(a)
	data.append(data_i)
"""
data = np.array(data)
df = pd.DataFrame({'District 1':data[0],'District 2':data[1],'District 3':data[2],'District 4':data[3],'District 5':data[4],'District 6':data[5],'District 7':data[6],'District 8':data[7],'District 9':data[8],'District 10':data[9],'District 11':data[10],'District 12':data[11],'District 13': data[12]})
ax = sns.violinplot(data = df)
plt.title('Uniform Distribution')
plt.xlabel('Districts (Ordered)')
plt.ylabel('Democrat Vote Margin')
plt.show()
"""

#SYMMETRIC CLUSTERING

##PLOT THE PDF
n = 16
p = .47
k = 2
data = []
for i in range(1,n+1):
	data_i = []
	for m in range(100):
		b = random.random()
		cdf_z = lambda x: sum(comb(n,j)*(binom.cdf(x,k,p))**j*(1-binom.cdf(x,k,p))**(n-j) for j in range(i,n+1)) - b
		a = optimize.brentq(cdf_z,-1,k)
		data_i.append(a/k)
	data.append(data_i)
newdata=[]
for i in range(len(data)):
        for j in range(len(data[i])):
                newdata.append([data[i][j],i+1,'order statistics'])
#newdata = np.array(newdata)
df=pd.DataFrame(newdata,columns=["Voting %", "District Number",'Type'])
#df = pd.DataFrame({'1.5':data[0],'2.5':data[1],'3.5':data[2],'4.5':data[3],'5.5':data[4],'6.5':data[5],'7.5':data[6],'8.5':data[7],'9.5':data[8],'10.5':data[9],'11.5':data[10],'12.5':data[11],'13.5': data[12], '14.5':data[13],'15.5':data[14], '16.5':data[15]})
statemap = toruskxk.makeKbyKMap(16, 16, 256)
data1 = toruskxk.simulateKbyK(statemap, 16, 63, 63)
for i in range(len(data1)):
	data1[i].append('torus')
df1 = pd.DataFrame(data, columns=["Voting %", "District Number",'Type']) 
df=pd.concat([df,df1])
print(df)

plt.figure()
ax = sns.boxplot(x="District Number", y="Voting %", hue="Type",data=df, palette="Set3")
plt.title('Least Democratic to Most Democratic District Vote Share Distribution (Small Correlation Length)')
plt.xlabel('Least Democratic to Most Democratic District (Ordered)')
plt.ylabel('Democrat Vote Share')
plt.savefig('boxplots16.png', bbox_inches='tight')
plt.close('all')






