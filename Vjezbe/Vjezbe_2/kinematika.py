import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F,m,tmax,dt):
    a=F/m
    T=[0]
    while T[-1]<=tmax:
        T.append(T[-1]+dt)

    if T[-1]>=tmax:
      T[-1]=tmax

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

def kosi_hitac(vo,kut,tmax,dt):
    ay=-9.81

    kut=np.deg2rad(kut)

    #Lista sa vremenima
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
