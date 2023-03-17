import numpy as np
import matplotlib.pyplot as plt

#Unos varijabli
F=float(input("Upisite iznos sile"))
m=float(input("Upisite iznos mase"))
a=F/m
tmax=10


#Lista sa vremenima
dt=0.01
T=[0]
while T[-1]<=10:
    T.append(T[-1]+dt)

if T[-1]>=10:
    T[-1]=10

#Lista sa akceleracijom
alist=[a]*len(T)

#Lista sa brzinom
v=[0]

i=0
while i<(len(T)-1):
    v.append(v[-1]+dt*a)
    i=i+1
    
#lista sa pomacima
j=0
x=[0]
while j<(len(T)-1):
    x.append(x[-1]+dt*v[j])
    j=j+1

#Plottanje
fig, axes = plt.subplots(1, 3, figsize=(10,4))

axes[0].plot(T,alist)
axes[0].set_title("a-t graf")
axes[0].set_xlabel('$t[s]$')
axes[0].set_ylabel('$a[m/s^{2}]$')

axes[1].plot(T,v)
axes[1].set_title("v-t graf")
axes[1].set_xlabel('$t[s]$')
axes[1].set_ylabel('$v[m/s]$')

axes[2].plot(T,x)
axes[2].set_title("x-t graf")
axes[2].set_xlabel('$t[s]$')
axes[2].set_ylabel('$x[m]$')
plt.show()