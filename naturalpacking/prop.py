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

#UNIFORM DISTRIBUTION
"""
##PROPORTIONALITY RATIO MULTIPLE P
n = 13
p_val = np.linspace(.2,.45,6)
sp = []
for p in p_val:
	s = []
	for k in range(11,101):
		sk = 0
		for i in range(1,n):
			j = i+1
			jd = lambda x,y: (math.factorial(n)/(math.factorial(i-1)*math.factorial(n-j))) * (norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**(i-1) * (1-norm.cdf(y,loc=p,scale=math.sqrt(p*(1-p)/k)))**(n-j) * (k/(2*math.pi*p*(1-p))) * math.e**((-k*(x-p)**2)/(2*p*(1-p))) * math.e**((-k*(y-p)**2)/(2*p*(1-p)))
			[a,b] = integrate.dblquad(jd,.5,1,0,.5)
			ai = a*i
			sk += ai
		sk += n * (norm.cdf(.5,loc=p,scale=math.sqrt(p*(1-p)/k)))**n
		sk = n - sk
		ss = sk/n
		prop = ss/p
		s.append(prop)
	sp.append(s)
k_log = []
for k in range(11,101):
	kl = -(np.log10(1/k))
	k_log.append(kl)
plt.figure()
fig,ax = plt.subplots()
ax.plot(k_log,sp[0],label='p = .2')
ax.plot(k_log,sp[1],label='p = .25')
ax.plot(k_log,sp[2],label='p = .3')
ax.plot(k_log,sp[3],label='p = .35')
ax.plot(k_log,sp[4],label='p = .4')
ax.plot(k_log,sp[5],label='p = .45')
legend = ax.legend(loc='upper left')
plt.title('Proportionality')
plt.xlabel('-log(1/k)')
plt.ylabel('Seat Share-Vote Share Ratio')
plt.savefig('propa.png', bbox_inches='tight')
plt.close('all')
"""
"""
##PROPORTIONALITY RATIO SINGLE P
n = 13
p = .47
s = []
for k in range(11,801):
	sk = 0
	for i in range(1,n):
		j = i+1
		jd = lambda x,y: (math.factorial(n)/(math.factorial(i-1)*math.factorial(n-j))) * (norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**(i-1) * (1-norm.cdf(y,loc=p,scale=math.sqrt(p*(1-p)/k)))**(n-j) * (k/(2*math.pi*p*(1-p))) * math.e**((-k*(x-p)**2)/(2*p*(1-p))) * math.e**((-k*(y-p)**2)/(2*p*(1-p)))
		[a,b] = integrate.dblquad(jd,.5,1,0,.5)
		ai = a*i
		sk += ai
	sk += n * (norm.cdf(.5,loc=p,scale=math.sqrt(p*(1-p)/k)))**n
	sk = n - sk
	ss = sk/n
	prop = ss/p
	s.append(prop)
k_log = []
for k in range(11,801):
	kl = -(np.log10(1/k))
	k_log.append(kl)
plt.figure()
fig,ax = plt.subplots()
ax.plot(k_log,s)
legend = ax.legend(loc='upper left')
plt.title('Proportionality')
plt.xlabel('-log(1/k)')
plt.ylabel('Seat Share-Vote Share Ratio')
plt.savefig('propk200.png', bbox_inches='tight')
plt.close('all')
"""

#SYMMETRIC CLUSTERING
"""
##PROPORTIONALITY RATIO MULTIPLE P
n = 13
p_val = np.linspace(.2,.45,6)
sp = []
k_odd = [1,3,5,7,9]
for p in p_val:
	s = []
	for k in k_odd:
		kf = math.floor(k/2)
		kc = math.ceil(k/2)
		sk = 0
		for i in range(1,n):
			j = i+1
			z = 0
			F = lambda x,y: sum((math.factorial(n)/(math.factorial(r)*math.factorial(s-r)*math.factorial(n-s))) * binom.cdf(x,k,p)**r * (binom.cdf(y,k,p)-binom.cdf(x,k,p))**(s-r) * (1-binom.cdf(y,k,p))**(n-s) for s in range(j,n+1) for r in range(i,s+1))
			for y in range(kc,k+1):
				for x in range(kf+1):
					q = F(x,y) - F(x-1,y) - F(x,y-1) + F(x-1,y-1)
					z += q
			sk += i*z
		sk += n * (binom.cdf(kf,k,p))**n
		sk = n - sk
		ss = sk/n
		prop = ss/p
		s.append(prop)
	sp.append(s)
k_log = []
for k in k_odd:
	kl = -(np.log10(1/k))
	k_log.append(kl)
plt.figure()
fig,ax = plt.subplots()
ax.plot(k_log,sp[0],label='p = .2')
ax.plot(k_log,sp[1],label='p = .25')
ax.plot(k_log,sp[2],label='p = .3')
ax.plot(k_log,sp[3],label='p = .35')
ax.plot(k_log,sp[4],label='p = .4')
ax.plot(k_log,sp[5],label='p = .45')
legend = ax.legend(loc='upper left')
plt.title('Proportionality')
plt.xlabel('-log(1/k)')
plt.ylabel('Seat Share-Vote Share Ratio')
plt.savefig('propsymmult.png', bbox_inches='tight')
plt.close('all')
"""
##PROPORTIONALITY RATIO SINGLE P
"""
n = 13
p = .47
s = []
k_odd = [1,3,5,7,9]
for k in k_odd:
	kf = math.floor(k/2)
	kc = math.ceil(k/2)
	sk = 0
	for i in range(1,n):
		j = i+1
		z = 0
		F = lambda x,y: sum((math.factorial(n)/(math.factorial(r)*math.factorial(s-r)*math.factorial(n-s))) * binom.cdf(x,k,p)**r * (binom.cdf(y,k,p)-binom.cdf(x,k,p))**(s-r) * (1-binom.cdf(y,k,p))**(n-s) for s in range(j,n+1) for r in range(i,s+1))
		for y in range(kc,k+1):
			for x in range(kf+1):
				q = F(x,y) - F(x-1,y) - F(x,y-1) + F(x-1,y-1)
				z += q
		sk += i*z
	sk += n * (binom.cdf(kf,k,p))**n
	sk = n - sk
	ss = sk/n
	prop = ss/p
	s.append(prop)
k_log = []
for k in k_odd:
	kl = -(np.log10(1/k))
	k_log.append(kl)
plt.figure()
fig,ax = plt.subplots()
ax.plot(k_log,s)
plt.title('Proportionality')
plt.xlabel('-log(1/k)')
plt.ylabel('Seat Share-Vote Share Ratio')
plt.savefig('propsym.png', bbox_inches='tight')
plt.close('all')
"""












