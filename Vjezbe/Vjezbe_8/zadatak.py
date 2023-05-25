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

    #Za vise odjednom
    def returnvalue(c):
        c.move()
        return c.x,c.y,c.z

    #Plottanje, ako zelimo da nam sam izbacuje dt, tj. pojedinacno
    def Plot(c):
        c.move()
        ax = plt.axes(projection='3d')
        ax.set_xlabel('x[m]')
        ax.set_ylabel('y[m]')
        ax.set_zlabel('z[m]')
        ax.set_title('Graf za dt={}'.format(c.dt))
        ax.plot3D(c.x,c.y,c.z,label='cool')
        plt.show()

#Ovo dalje se moze u zasebnom dokumentu

#Usporedba razl. koraka odjednom, ako zelimo jedan po jedan samo koristimo Plot definiran ranije
#Nije potrebno nuzno ove x1,y1,z1, moze se i direkno u plot3D ali ovako mi je citljivije
#Ako weird ispadnu usporedbe, moze se tweakat virjednosti np krace vrijeme ili manji naboj/masa
c1=Cestica(np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),2,2,0.01,40)
x1,y1,z1=c1.returnvalue()
c2=Cestica(np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),2,2,0.1,40)
x2,y2,z2=c2.returnvalue()
c3=Cestica(np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),2,2,0.2,40)
x3,y3,z3=c3.returnvalue()

ax = plt.axes(projection='3d')

ax.plot3D(x1,y1,z1)
ax.plot3D(x2,y2,z2)
ax.plot3D(x3,y3,z3)

ax.set_xlabel('x[m]')
ax.set_ylabel('y[m]')
ax.set_zlabel('z[m]')
ax.set_title('Graf ovisan o dt-u, po Euleru')
ax.legend(['dt=0.01','dt=0.1','dt=0.2'])
plt.show()



#Usporedba elektrona i pozitrona - elektron je - naboj
c4=Cestica(np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),2,2,0.01,40)
x4,y4,z4=c4.returnvalue()
c5=Cestica(np.array((0,0,0)),np.array((0,0,0)),np.array((0,0,1)),np.array((0.1,0.1,0.1)),-2,2,0.01,40)
x5,y5,z5=c5.returnvalue()

ax=plt.axes(projection='3d')
ax.plot3D(x4,y4,z4)
ax.plot3D(x5,y5,z5)

ax.set_title('Graf elektrona i pozitrona za dt=0.01')
ax.legend(['Pozitron','Elektron'])
plt.show()