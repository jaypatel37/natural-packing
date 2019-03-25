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

#UNIFORMLY DISTRIBUTED

##PLOT THE PDF
"""
n = 13
p = .47
k = 100
data = []
for i in range(1,n+1):
	data_i = []
	for m in range(100): 
		b = random.random()
		cdf_z = lambda x: sum(comb(n,j) * (norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**j * (1-norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**(n-j) for j in range(i,n+1)) - b
		a = optimize.brentq(cdf_z,0,1)
		data_i.append(a)
	data.append(data_i)
data = np.array(data)
df = pd.DataFrame({'District 1':data[0],'District 2':data[1],'District 3':data[2],'District 4':data[3],'District 5':data[4],'District 6':data[5],'District 7':data[6],'District 8':data[7],'District 9':data[8],'District 10':data[9],'District 11':data[10],'District 12':data[11],'District 13': data[12]})
ax = sns.violinplot(data = df)
plt.title('Uniform Distribution')
plt.xlabel('Disrtricts (Ordered)')
plt.ylabel('Democrat Vote Margin')
plt.show()
"""

#SYMMETRIC CLUSTERING
##PLOT THE PDF
"""
n = 13
p = .47
k = 5
data = []
for i in range(1,n+1):
	data_i = []
	for m in range(100):
		b = random.random()
		cdf_z = lambda x: sum(comb(n,j)*(binom.cdf(x,k,p))**j*(1-binom.cdf(x,k,p))**(n-j) for j in range(i,n+1)) - b
		a = optimize.brentq(cdf_z,-1,k)
		data_i.append(a/k)
	data.append(data_i)
data = np.array(data)
df = pd.DataFrame({'District 1':data[0],'District 2':data[1],'District 3':data[2],'District 4':data[3],'District 5':data[4],'District 6':data[5],'District 7':data[6],'District 8':data[7],'District 9':data[8],'District 10':data[9],'District 11':data[10],'District 12':data[11],'District 13': data[12]})
ax = sns.violinplot(data = df)
plt.title('Symmetric Clustering')
plt.xlabel('Disrtricts (Ordered)')
plt.ylabel('Democrat Vote Margin')
plt.show()
"""



