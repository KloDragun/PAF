#Ovo radim proceduralno jer nema smisla ovo u klase/funkcije jer se samo jednom mora izvrtit
import numpy as np
import matplotlib.pyplot as plt

#Inicijalizacija
G= 6.67408*10**-11
year=365.242*24*60*60

r_Earth=[np.array((1.486*10**11,0))]
v_Earth=[np.array((0,29783))]
a_Earth=[]
x_Earth=[]
y_Earth=[]

r_Sun=[np.array((0,0))]
v_Sun=[np.array((0,0))]
a_Sun=[]
x_Sun=[]
y_Sun=[]

m_Earth= 5.9742*10**24
m_Sun=1.989*10**30

#dt u sekundama
dt=3600
#
for i in np.arange(0,year,dt):
    a_Sun.append(-G*m_Earth*(r_Sun[-1]-r_Earth[-1])/(np.sqrt(np.dot((r_Sun[-1]-r_Earth[-1]),(r_Sun[-1]-r_Earth[-1]))))**3)
    v_Sun.append(v_Sun[-1]+a_Sun[-1]*dt)
    r_Sun.append(r_Sun[-1]+v_Sun[-1]*dt)

    a_Earth.append(-G*m_Sun*(r_Earth[-1]-r_Sun[-1])/(np.sqrt(np.dot((r_Sun[-1]-r_Earth[-1]),(r_Sun[-1]-r_Earth[-1]))))**3)
    v_Earth.append(v_Earth[-1]+a_Earth[-1]*dt)
    r_Earth.append(r_Earth[-1]+v_Earth[-1]*dt)

#Preuzimam x i y koord iz r-a
for i in range(len(r_Earth)):
    x_Sun.append(r_Sun[i][0])
    y_Sun.append(r_Sun[i][1])
    x_Earth.append(r_Earth[i][0])
    y_Earth.append(r_Earth[i][1])

#Plottanje
plt.plot(x_Earth,y_Earth)
plt.plot(x_Sun,y_Sun)
plt.title("Simulacija Sunca i Zemlje")
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.legend(['Zemlja','Sunce'])
plt.show()