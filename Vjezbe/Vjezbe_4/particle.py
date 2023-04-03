import numpy as np
import matplotlib.pyplot as plt
g=9.81
class Particle:

    def __init__(c,v,fi,x,y,dt):
        c.brzina=v
        c.kut=np.deg2rad(fi)
        c.koordx=[x]
        c.koordy=[y]
        c.brzinay=[v*np.sin(c.kut)]
        c.tuk=0
        c.domet=0
        c.dt=dt
        c.andomet=0
    def reset(c):
        c.koordx=[c.koordx[0]]
        c.koordy=[c.koordy[0]]
        c.brzinay=[c.brzinay[0]]
        c.tuk=0
        c.domet=0
    
    #Ovaj reset se koristi kod range f-je
    def tempreset(c):
        c.koordx=[c.koordx[0]]
        c.koordy=[c.koordy[0]]
        c.brzinay=[c.brzinay[0]]
        c.tuk=0

    def __move(c):
        c.tuk=c.tuk+c.dt
        c.brzinay.append(c.brzinay[-1]-g*c.dt)
        c.koordx.append(c.koordx[-1]+c.brzina*c.dt*np.cos(c.kut))
        c.koordy.append(c.koordy[-1]+c.brzinay[-1]*c.dt)

    def evolve(c):
        while(c.koordy[-1]>=0):
            c.__move()

        del c.brzinay[-1]
        del c.koordx[-1]
        del c.koordy[-1]

    def range(c):
        c.evolve()
        c.domet=c.koordx[-1]
        c.tempreset()
        return c.domet

    def plot_trajectory(c):
        c.evolve()
        plt.plot(c.koordx,c.koordy)
        plt.title("x-y graf")
        plt.xlabel("x-os [m]")
        plt.ylabel("y-os [m]")
        plt.show()
        c.reset()

    def analiticko(c):
        c.evolve()
        c.andomet=c.tuk*c.brzina*np.cos(c.kut)
        c.tempreset()
        return c.andomet