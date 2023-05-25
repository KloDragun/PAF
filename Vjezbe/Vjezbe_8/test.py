import numpy as np
import matplotlib.pyplot as plt

class Cestica():

    #Deklaracije
    def __init__(c,p,E,B,v,q,m,dt,t):
        c.E=E
        c.B=B
        c.q=q
        c.m=m
        c.dt=dt
        c.p=[p]
        c.v=[v]
        c.a=[(c.q/c.m)*(c.E+np.cross(c.v[0],c.B))]
        c.x=[]
        c.y=[]
        c.z=[]
        c.t=t

    
    def move(c):
        #Za svaku tocku od 0 pa do odredenog t udaljeno za dt updatea polozaj,brzinu i akcel
        for i in np.arange(0,c.t,c.dt):
            c.p.append(c.p[-1]+c.v[-1]*c.dt)
            c.v.append(c.v[-1]+c.a[-1]*c.dt)
            c.a.append((c.q/c.m)*(c.E+np.cross(c.v[-1],c.B)))
        
        #Jer p sadrzi vise lista prva zagrada se krece po listama a druga po varijablama (x,y,z)
        for i in range(len(c.p)):
            c.x.append(c.p[i][0])
            c.y.append(c.p[i][1])
            c.z.append(c.p[i][2])


    def Plot(c):
        c.move()
        print(c.x)
        print(c.y)
        print(c.z)
        ax = plt.axes(projection='3d')

        ax.plot3D(c.x,c.y,c.z,label='test')
        plt.show()
        

p1=Cestica(np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),2,2,0.1,40)
p1.Plot()