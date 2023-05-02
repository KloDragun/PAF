import harmonic_oscillator as har
import matplotlib.pyplot as plt
import numpy as np

#Za lako testiranje
m=1
k=20

test1=har.HarmonicOscillator(m,k,0,0.1,0.01,10)
test1.move()
test2=har.HarmonicOscillator(m,k,0,0.1,0.1,10)
test2.move()
test3=har.HarmonicOscillator(m,k,0,0.1,0.25,10)
test3.move()

#Analiticki
A=np.sqrt((test1.x[0]**2)+((m/k)*((test1.v[0])**2)))
w=np.sqrt(k/m)
fi=np.arcsin(test1.x[0]/A)

t=np.linspace(0,10,1000)
analiticko=[]
for i in t:
    analiticko.append(A*np.sin(w*i+fi))

#Plottanje
fig, ax = plt.subplots(figsize=(12,12))

ax.plot(t,analiticko, linewidth=2,color='red',label='Analiticki')
ax.scatter(test1.t,test1.x,label='dt=0.01',s=11)
ax.scatter(test2.t,test2.x,label='dt=0.1',s=11)
ax.scatter(test3.t,test3.x,label='dt=0.25',color='purple',s=11)

ax.set_title('x-t graf ovisno o koraku')
ax.set_xlabel('t[s]')
ax.set_ylabel('x[m]')

ax.legend()
plt.show()

