import scipy
import math
from scipy.stats import norm
import scipy.integrate as integrate
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.special import comb
from scipy.stats import binom
import chartDrawer
import toruskxk

#SIMULATED THROUGH TORUS SLOPE

statemap = toruskxk.makeKbyKMap(1, 16, 256)
data = toruskxk.simulateKbyK(statemap, 16, 63, 63)
k1=[2,4,8,16]
slope1=[]
for item in k1:
    statemap = toruskxk.makeKbyKMap(item, 16, 256)
    data = toruskxk.simulateKbyK(statemap, 16, 63, 63)
    slope1.append(chartDrawer.calcSlope(data,16))

"""

#SYMMETRIC CLUSTERING
"""
####SLOPE PROBABILITY
##p = .47
##n = 13
##slope = []
##a = np.linspace(0,1/n,100)
##for k in [1,3,7,10]:
##	sk = []
##	for s in a:
##		m_val = np.linspace(0,(1-n*s)*k,100)
##		jd = sum(((binom.cdf((n*s+m)*k,k,p)-binom.cdf((m*k)-1,k,p))**n - (binom.cdf((n*s+m)*k,k,p)-binom.cdf(m*k,k,p))**n - (binom.cdf(((n*s+m)*k)-1,k,p)-binom.cdf((m*k)-1,k,p))**n + (binom.cdf(((n*s+m)*k)-1,k,p)-binom.cdf(m*k,k,p))**n) for m in m_val)
##		sk.append(jd)
##	slope.append(sk)
##plt.figure()
##fig,ax = plt.subplots()
###ax.plot(a,slope[0],label='k=1')
###ax.plot(a,slope[1],label='k=3')
##ax.plot(a,slope[2],'g',label='k=7')
##ax.plot(a,slope[3],'r',label='k=10')
##legend = ax.legend(loc='upper left')
##plt.axis([0,.08,0,3])
##plt.title('Slope Probability')
##plt.xlabel('slope')
##plt.ylabel('pdf')
##plt.savefig('slopeprob_symm_a.png', bbox_inches='tight')
##plt.close('all')
"""
"""
##SLOPE
p = .47
n = 16
slope = []
for k in range(1,21):
	M = sum(1-(binom.cdf(x,k**2,p))**n for x in range(k**2))/(k**2)
	m = sum((1-binom.cdf(x,k**2,p))**n for x in range(k**2))/(k**2)
	slope_k = (M-m)/n
	slope.append(slope_k)
##plt.figure()
##fig,ax = plt.subplots()
##ax.plot(range(1,11),slope,label='Slope')
##legend = ax.legend(loc='upper left')
##plt.title('Slope')
##plt.xlabel('k')
##plt.ylabel('slope')
##plt.savefig('slope_symm.png', bbox_inches='tight')
##plt.close('all')


#UNIFORMLY DISTRIBUTED

##SLOPE PROBABILITY
##p = .47
##n = 16
##slope = []
##a = np.linspace(0,1/n,100)
##for k in [11,50,300,1000]:
##	sk = []
##	for s in a:
##		jd = lambda m: n * (n-1) * (norm.cdf((n*s+m),loc=p,scale=math.sqrt(p*(1-p)/k))-norm.cdf(m,loc=p,scale=math.sqrt(p*(1-p)/k)))**(n-2) * (k/(2*math.pi*p*(1-p))) * math.e**((-k*((m-p)**2)/(2*p*(1-p)))) * math.e**((-k*((n*s+m-p)**2))/(2*p*(1-p)))
##		[c,d] = integrate.quadrature(jd,0,1-n*s)
##		sk.append(c)
##	slope.append(sk)
##plt.figure()
##fig,ax = plt.subplots()
##ax.plot(a,slope[0],label='k=11')
##ax.plot(a,slope[1],label='k=50')
##ax.plot(a,slope[2],label='k=300')
##ax.plot(a,slope[3],label='k=1000')
##legend = ax.legend(loc='upper left')
##plt.title('Slope Probability')
##plt.xlabel('slope')
##plt.ylabel('pdf')
##plt.savefig('slopeprob.png', bbox_inches='tight')
##plt.close('all')
"""
"""
##SLOPE
##p = .47
##n = 16
####slope = []
##for k in range(3,21):
##	max_mean = lambda x: x * (n*math.sqrt(k**2))/(math.sqrt(2*math.pi*p*(1-p))) * (norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/(k**2))))**(n-1) * math.e**((-(k**2)*(x-p)**2)/(2*p*(1-p)))
##	[M,c] = integrate.quadrature(max_mean,0,1)
##	min_mean = lambda y: y * (n*math.sqrt(k**2))/(math.sqrt(2*math.pi*p*(1-p))) * (1-norm.cdf(y,loc=p,scale=math.sqrt(p*(1-p)/(k**2))))**(n-1) * math.e**((-(k**2)*(y-p)**2)/(2*p*(1-p)))
##	[m,b] = integrate.quadrature(min_mean,0,1)
##	slope_k = (M-m)/n
##	slope.append(slope_k)
plt.figure()
fig,ax = plt.subplots()
ax.plot(range(1,21),slope,color='blue', label='Order Statistics')
ax.plot(k1,slope1,'ro', label="Torus")
legend = ax.legend(loc='upper left')
plt.title('Slope versus K')
plt.xlabel('k')
plt.ylabel('Slope')
plt.savefig('slopecomparison.png', bbox_inches='tight')
plt.close('all')



