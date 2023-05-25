import numpy as np
import matplotlib.pyplot as plt

class Projectile:

    #Inicijalizacija
    def __init__(c,v,fi,x,y,dt,ro,Cd,A,m):
        c.brzina=v
        c.ro=ro
        c.Cd=Cd
        c.m=m
        c.A=A
        c.kut=np.deg2rad(fi)
        c.koordx=[x]
        c.koordy=[y]
        c.brzinay=[v*np.sin(c.kut)]
        c.brzinax=[v*np.cos(c.kut)]
        c.akcelx=[-1*np.sign(c.brzinax[0])*(c.ro*c.Cd*c.A/(2*c.m))*(c.brzinax[0])**2]
        c.akcely=[-9.81-np.sign(c.brzinay[0])*(c.ro*c.Cd*c.A/(2*c.m))*(c.brzinay[0])**2]

        c.dt=dt

    #Euler
    def Euler_move(c):
        while c.koordy[-1]>=0:
            c.koordx.append(c.koordx[-1]+c.brzinax[-1]*c.dt)
            c.koordy.append(c.koordy[-1]+c.brzinay[-1]*c.dt)
            c.brzinax.append(c.brzinax[-1]+c.akcelx[-1]*c.dt)
            c.brzinay.append(c.brzinay[-1]+c.akcely[-1]*c.dt)
            c.akcelx.append(-1*np.sign(c.brzinax[-1])*(c.ro*c.Cd*c.A/(2*c.m))*(c.brzinax[-1])**2)
            c.akcely.append(-9.81-np.sign(c.brzinay[-1])*(c.ro*c.Cd*c.A/(2*c.m))*(c.brzinay[-1])**2)


    #R-k
    def RungeKutta_Move(c):
        while c.koordy[-1]>=0:
            kvx=[(-1*np.sign(c.brzinax[-1])*(c.ro*c.Cd*c.A/(2*c.m))*(c.brzinax[-1])**2)*c.dt]
            kvy=[(-9.81-np.sign(c.brzinay[-1])*(c.ro*c.Cd*c.A/(2*c.m))*(c.brzinay[-1])**2)*c.dt]
            kx=[c.brzinax[-1]*c.dt]
            ky=[c.brzinay[-1]*c.dt]
        
            for i in range(3):
                kvx.append((-1*np.sign(c.brzinax[-1]+0.5*kvx[-1])*(c.ro*c.Cd*c.A/(2*c.m))*(c.brzinax[-1]+0.5*kvx[-1])**2)*c.dt)
                kvy.append((-9.81-np.sign(c.brzinay[-1]+0.5*kvy[-1])*(c.ro*c.Cd*c.A/(2*c.m))*(c.brzinay[-1]+kvy[-1])**2)*c.dt)
                kx.append((c.brzinax[-1]+0.5*kvx[-1])*c.dt)
                ky.append((c.brzinay[-1]+0.5*kvy[-1])*c.dt)
                
            c.brzinax.append(c.brzinax[-1]+(kvx[0]+2*kvx[1]+2*kvx[2]+kvx[3])/6)
            c.brzinay.append(c.brzinay[-1]+(kvy[0]+2*kvy[1]+2*kvy[2]+kvy[3])/6)
            c.koordx.append(c.koordx[-1]+(kx[0]+2*kx[1]+2*kx[2]+kx[3])/6)
            c.koordy.append(c.koordy[-1]+(ky[0]+2*ky[1]+2*ky[2]+ky[3])/6)



    #Plottanje
    def Plot(c,Rk=1):
        if Rk==1:
            c.RungeKutta_Move()
            plt.plot(c.koordx,c.koordy)
            plt.title("x-y graf")
            plt.xlabel("x [m]")
            plt.ylabel("y [m]")
        else:
            c.Euler_move()
            plt.plot(c.koordx,c.koordy)
            plt.title("x-y graf")
            plt.xlabel("x [m]")
            plt.ylabel("y [m]")



    
#Inputi za plottanje ,moze se i u drugi file pa importat projectile al pri ruci mi je
t1=Projectile(10,20,0,0,0.001,2.3,0.6,0.05,4)
t2=Projectile(10,20,0,0,0.1,2.3,0.6,0.05,4)
t3=Projectile(10,20,0,0,0.2,2.3,0.6,0.05,4)
t4=Projectile(10,20,0,0,0.01,2.3,0.6,0.05,4)
t5=Projectile(10,20,0,0,0.01,2.3,0.6,0.05,4)

t1.Plot(2)
t2.Plot(2)
t3.Plot(2)
t4.Plot(2)
t5.Plot()


plt.legend(['dt=0.001 s', 'dt=0.1s', 'dt=0.2s','dt=0.01s', 'dt=0.01s, Rk'])
plt.show()


#Kao što se iz grafa vidi, nefizičko gibanje imamo za dt=0.2(ili priblizno tome)
#Iz slike se vidi da je Runge-Kutteova metoda preciznija(Rk je blize 0.001)
