import numpy as np
import matplotlib.pyplot as plt

#Unos varijabla i postavljanje liste vremena
vo=float(input("Upisite pocetnu brzinu"))
kut=float(input("Upisite kut(stupnjevi)"))
tmax=10
ay=-9.81

#Konverzija u radijane
kut=np.deg2rad(kut)

#Lista sa vremenima
dt=0.01
T=[0]
while T[-1]<=tmax:
    T.append(T[-1]+dt)
if T[-1]>=tmax:
    T[-1]=tmax

#Lista sa pomacima po x osi
x=[0]
j=0
while j<(len(T)-1):
    x.append(x[-1]+dt*vo*np.cos(kut))
    j=j+1


#Lista sa promjenama brzine u y smjeru
voy=[vo*np.sin(kut)]
k=0
while k<(len(T)-1):
    voy.append(voy[-1]+ay*dt)
    k=k+1



#Lista sa pomacima po y osi
y=[0]
i=0
while i<(len(T)-1):
    y.append(y[-1]+dt*voy[i])
    i=i+1

#Plottanje
fig, axes = plt.subplots(1, 3, figsize=(10,4))

axes[0].plot(x,y)
axes[0].set_title("x-y graf")
axes[0].set_xlabel('$x[m]$')
axes[0].set_ylabel('$y[m]$')

axes[1].plot(T,x)
axes[1].set_title("x-t graf")
axes[1].set_xlabel('$t[s]$')
axes[1].set_ylabel('$x[m]$')

axes[2].plot(T,y)
axes[2].set_title("y-t graf")
axes[2].set_xlabel('$t[s]$')
axes[2].set_ylabel('$y[m]$')
plt.show()