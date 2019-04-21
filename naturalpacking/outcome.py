import scipy
import math
from scipy.stats import norm
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

#SAFE DISTRICTS: districts that are Democrat or Republican with 60% Probability

#UNIFORMLY DISTRIBUTED
"""
##PROBABILITY EACH DISTRICT IS REPUBLICAN
p = .47
n = 13
x = .5
prob = []
for k in (11,50,300,1000):
	a = []
	for i in range(1,n+1):
		cdf = sum(comb(n,j) * (norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**j * (1-norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**(n-j) for j in range(i,n+1))
		a.append(cdf)
	prob.append(a)
plt.figure()
fig,ax = plt.subplots()
ax.plot(range(1,n+1),prob[0],'-o', label='k=11')
ax.plot(range(1,n+1),prob[1],'-o',label='k=50')
ax.plot(range(1,n+1),prob[2],'-o',label='k=300')
ax.plot(range(1,n+1),prob[3],'-o',label='k=1000')
legend = ax.legend(loc='upper left')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13], ['D(1)','D(2)','D(3)','D(4)','D(5)','D(6)','D(7)','D(8)','D(9)','D(10)','D(11)','D(12)','D(13)',])
plt.title('Probability of Republican District')
plt.xlabel('Districts (Ordered)')
plt.ylabel('Probability')
plt.savefig('repub.png', bbox_inches='tight')
plt.close('all')
"""
"""
##PROBABILITY EACH DISTRICT IS DEMOCRAT
p = .47
n = 13
x = .5
prob_d = []
for k in (11,50,300,1000):
	a_d = []
	for i in range(1,n+1):
		cdf_d = sum(comb(n,j) * (norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**j * (1-norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**(n-j) for j in range(i,n+1))
		cdf_d = 1 - cdf_d
		a_d.append(cdf_d)
	prob_d.append(a_d)
plt.figure()
fig,ax = plt.subplots()
ax.plot(range(1,n+1),prob_d[0],'-o', label='k=11')
ax.plot(range(1,n+1),prob_d[1],'-o',label='k=50')
ax.plot(range(1,n+1),prob_d[2],'-o',label='k=300')
ax.plot(range(1,n+1),prob_d[3],'-o',label='k=1000')
legend = ax.legend(loc='upper left')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13], ['D(1)','D(2)','D(3)','D(4)','D(5)','D(6)','D(7)','D(8)','D(9)','D(10)','D(11)','D(12)','D(13)',])
plt.title('Probability of Democrat District')
plt.xlabel('Districts (Ordered)')
plt.ylabel('Probability')
plt.savefig('dems.png', bbox_inches='tight')
plt.close('all')
"""
"""
##NUMBER OF SAFE DISTRICTS
p = .47
n = 13
x = .5
safe_dist = []
safe_rep = []
for k in range(11,1001):
	safe_rep_count = 0
	for i in range(1,n+1):
		cdf = sum(comb(n,j) * (norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**j * (1-norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**(n-j) for j in range(i,n+1))
		if cdf >= .6:
			safe_rep_count += 1
	safe_rep.append(safe_rep_count)
safe_dist.append(safe_rep)
safe_dem = []
for k in range(11,1001):
	safe_dem_count = 0
	for i in range(1,n+1):
		cdf = sum(comb(n,j) * (norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**j * (1-norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**(n-j) for j in range(i,n+1))
		if cdf <= .4:
			safe_dem_count += 1
	safe_dem.append(safe_dem_count)
safe_dist.append(safe_dem)
plt.figure()
fig,ax = plt.subplots()
ax.plot(range(11,1001),safe_dist[0],'r',label='Republican')
ax.plot(range(11,1001),safe_dist[1],'b',label='Democrat')
legend = ax.legend(loc='upper left')
plt.axis([11,1000,0,n])
plt.title('Safe Districts')
plt.xlabel('Number of Units')
plt.ylabel('Number of Districts')
plt.savefig('safedist.png', bbox_inches='tight')
plt.close('all')
"""

#SYMMETRICALLY CLUSTERED
"""
##PROBABILITY EACH DISTRICT IS REPUBLICAN
p = .47
n = 13
prob = []
for k in (1,3,7,10):
	x = k/2
	a = []
	for i in range(1,n+1):
		cdf = sum(comb(n,j)*(binom.cdf(x,k,p))**j*(1-binom.cdf(x,k,p))**(n-j) for j in range(i,n+1))
		a.append(cdf)
	prob.append(a)
plt.figure()
fig,ax = plt.subplots()
ax.plot(range(1,n+1),prob[0],'-o', label='k=1')
ax.plot(range(1,n+1),prob[1],'-o',label='k=3')
ax.plot(range(1,n+1),prob[2],'-o',label='k=7')
ax.plot(range(1,n+1),prob[3],'-o',label='k=10')
legend = ax.legend(loc='upper left')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13], ['D(1)','D(2)','D(3)','D(4)','D(5)','D(6)','D(7)','D(8)','D(9)','D(10)','D(11)','D(12)','D(13)',])
plt.title('Probability of Republican District')
plt.xlabel('Districts (Ordered)')
plt.ylabel('Probability')
plt.savefig('repub_sym.png', bbox_inches='tight')
plt.close('all')
"""
"""
##PROBABILITY EACH DISTRICT IS DEMOCRAT
p = .47
n = 13
prob = []
for k in (1,3,7,10):
	x = k/2
	a = []
	for i in range(1,n+1):
		cdf = sum(comb(n,j)*(binom.cdf(x,k,p))**j*(1-binom.cdf(x,k,p))**(n-j) for j in range(i,n+1))
		cdf = 1-cdf
		a.append(cdf)
	prob.append(a)
plt.figure()
fig,ax = plt.subplots()
ax.plot(range(1,n+1),prob[0],'-o', label='k=1')
ax.plot(range(1,n+1),prob[1],'-o',label='k=3')
ax.plot(range(1,n+1),prob[2],'-o',label='k=7')
ax.plot(range(1,n+1),prob[3],'-o',label='k=10')
legend = ax.legend(loc='upper left')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13], ['D(1)','D(2)','D(3)','D(4)','D(5)','D(6)','D(7)','D(8)','D(9)','D(10)','D(11)','D(12)','D(13)',])
plt.title('Probability of Democrat District')
plt.xlabel('Districts (Ordered)')
plt.ylabel('Probability')
plt.savefig('dems_sym.png', bbox_inches='tight')
plt.close('all')
"""
"""
##NUMBER OF SAFE DISTRICTS
p = .47
n = 13
safe_dist = []
safe_rep = []
for k in range(1,11):
	x = k/2
	safe_rep_count = 0
	for i in range(1,n+1):
		cdf = sum(comb(n,j)*(binom.cdf(x,k,p))**j*(1-binom.cdf(x,k,p))**(n-j) for j in range(i,n+1))
		if cdf >= .6:
			safe_rep_count += 1
	safe_rep.append(safe_rep_count)
safe_dist.append(safe_rep)
safe_dem = []
for k in range(1,11):
	x = k/2
	safe_dem_count = 0
	for i in range(1,n+1):
		cdf = sum(comb(n,j)*(binom.cdf(x,k,p))**j*(1-binom.cdf(x,k,p))**(n-j) for j in range(i,n+1))
		if cdf <= .4:
			safe_dem_count += 1
	safe_dem.append(safe_dem_count)
safe_dist.append(safe_dem)
plt.figure()
fig,ax = plt.subplots()
ax.plot(range(1,11),safe_dist[0],'r',label='Republican')
ax.plot(range(1,11),safe_dist[1],'b',label='Democrat')
legend = ax.legend(loc='upper left')
plt.axis([1,10,0,n])
plt.title('Safe Districts')
plt.xlabel('Number of Units')
plt.ylabel('Number of Districts')
plt.savefig('safedist_symm.png', bbox_inches='tight')
plt.close('all')
"""






