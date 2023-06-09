#Modificirana verzija Projectile.py sa vjezbe 7

import numpy as np

class Projectile:

    #Inicijalizacija
    def __init__(c,v,fi,x,y,dt,ro,A,Cd,m):
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

        c.dt=dt

    #R-k, modificirana da vraća arrayeve sa x i y koordinatama
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
        return c.koordx,c.koordy
    

#Makao sam plottanje jer uzimamo direktno iz Rk move-a, i daljnja plotanja radimo u zasebnom file-u
        

