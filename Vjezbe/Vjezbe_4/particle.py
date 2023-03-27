import numpy as np
g=9.81
class Particle:
    def __init__(c,v,fi,x,y):
        c.brzina=v
        c.kut=fi
        c.koordx=x
        c.koordy=y

    def print(c):
        print(c.brzina)
        print(c.kut)
        print(c.koordx,c.koordy)

    def reset(c):
        c.brzina=0
        c.kut=0
        c.koord=0

    def __move(c):
        dt=0.02
        c.koordx=c.koordx+c.brzina*dt*np.cos(c.kut)
        c.koordy=c.koordy+c.brzina*dt*np.sin(c.kut)-0.5*g*(dt**2) #analiticki, ne ovako

    def evolve(c):
        while(c.koordy>0):
            c.__move()


p1=Particle(10,60,2,3)
p1.print()
p1.evolve()
p1.print()
