import scipy
import math
from scipy.stats import norm
from scipy.special import comb
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.integrate as integrate
from scipy.stats import binom
import toruskxk
import chartDrawer

#TORUS
n = 16
k = 8
p1=[i for i in range(101)]
votes=[]
for p in range(len(p1)):
    statemap = toruskxk.makeKbyKMap(k, 16, 128,p1[p])
    data = toruskxk.simulateKbyK(statemap, 16, 63, 63)
    votes.append(chartDrawer.averageSeatShare(data,n))
    p1[p]=p1[p]/float(100)
    


#UNIFORMLY DISTRIBUTED
"""
##EXPECTED NUMBER OF DISTRICTS
p = .47
n = 13
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
	s.append(sk)
k_log = []
for k in range(11,801):
	kl = -(np.log10(1/k))
	k_log.append(kl)
plt.figure()
fig,ax = plt.subplots()
ax.plot(k_log,s,label='Expected Number of Seats')
legend = ax.legend(loc='upper left')
plt.title('Expected Number of Seats')
plt.xlabel('-log(1/k)')
plt.ylabel('Number of Seats')
plt.savefig('avgseatslog.png', bbox_inches='tight')
plt.close('all')
"""
"""
##VOTE SEAT CURVE
n = 16
k = 4
s = []
z = np.linspace(.4,.6,100)
for p in z:
	sk = 0
	for i in range(1,n):
		j = i+1
		jd = lambda x,y: (math.factorial(n)/(math.factorial(i-1)*math.factorial(n-j))) * (norm.cdf(x,loc=p,scale=math.sqrt(p*(1-p)/k)))**(i-1) * (1-norm.cdf(y,loc=p,scale=math.sqrt(p*(1-p)/k)))**(n-j) * (k/(2*math.pi*p*(1-p))) * math.e**((-k*(x-p)**2)/(2*p*(1-p))) * math.e**((-k*(y-p)**2)/(2*p*(1-p)))
		[a,b] = integrate.dblquad(jd,.5,1,0,.5)
		ai = a*i
		sk += ai
	sk += n * (norm.cdf(.5,loc=p,scale=math.sqrt(p*(1-p)/k)))**n
	sk = n - sk
	s.append(sk)
y = []
for p in z:
	y.append(p*n)
plt.figure()
fig,ax = plt.subplots()
ax.plot(z,s,'b',label='Expected Number of Seats')
ax.plot(z,y,'g',label = 'Proportionality')
legend = ax.legend(loc='upper left')
plt.title('Vote-Seat Curve (Democrats)')
plt.xlabel('Democrat Vote Fraction')
plt.ylabel('Number of Democrat Seats')
plt.savefig('voteseatsda.png', bbox_inches='tight')
plt.close('all')
"""

#SYMMETRIC CLUSTERING
"""
##EXPECTED NUMBER OF DISTRICTS
n = 13
p = .47
s = []
k_odd = [1,3,5,7,9]
#k_even = [2,4,6,8,10]
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
	s.append(sk)
k_odd_log = []
for k in k_odd:
	kl = -(np.log10(1/k))
	k_odd_log.append(kl)
plt.figure()
fig,ax = plt.subplots()
ax.plot(k_odd_log,s,label='Expected Number of Republican Seats')
legend = ax.legend(loc='upper left')
plt.title('Expected Number of Republican Seats')
plt.xlabel('-log(1/k)')
plt.ylabel('Number of Seats')
plt.savefig('avgseatslogsym.png', bbox_inches='tight')
plt.close('all')
"""

##VOTE SEAT CURVE
n = 16
k = 7
kf = math.floor(k/2)
kc = math.ceil(k/2)
s = []
w = np.linspace(0,1,100)
for p in w:
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
	sk = n-sk
	s.append(sk)
y = []
for p in w:
	y.append(p*n)
plt.figure()
fig,ax = plt.subplots()
ax.plot(w,s,'b',label='Order Statistics Expectation')
ax.plot(w,y,'g',label = 'Proportionality')
ax.plot(p1,votes,'r',label='Torus Expectation')
legend = ax.legend(loc='upper left')
plt.title('Vote-Seat Curve (k=8)')
plt.xlabel('Democrat Vote Fraction')
plt.ylabel('Number of Democrat Seats')
plt.savefig('voteseat8.png', bbox_inches='tight')
plt.close('all')







