import harmonic_oscillator as har
import numpy as np
import matplotlib.pyplot as plt



m=2
k=100

test1=har.HarmonicOscillator(m,k,20,3,0.001,10)
a,t1=test1.period()
test2=har.HarmonicOscillator(m,k,20,3,0.01,10)
b,t2=test2.period()
test3=har.HarmonicOscillator(m,k,20,3,0.05,10)
c,t3=test3.period()
test4=har.HarmonicOscillator(m,k,20,3,0.1,10)
d,t4=test4.period()
test5=har.HarmonicOscillator(m,k,20,3,0.2,10)
e,t5=test5.period()
print(a,b,c)
w=np.sqrt(test1.k/test1.m)
T=(2*np.pi/w)
print(T)
testmat=[]
for i in test1.t:
    testmat.append(T)
fig, ax = plt.subplots(figsize=(12,12))

ax.plot(test1.t,testmat, linewidth=2,color='red',label='Analiticki')
ax.scatter(test1.t[t1],a,label='dt=0.001',s=11)
ax.scatter(test2.t[t2],b,label='dt=0.01',s=11)
ax.scatter(test3.t[t3],c,label='dt=0.05',color='black',s=11)
ax.scatter(test4.t[t4],d,label='dt=0.1',color='purple',s=11)
ax.scatter(test5.t[t5],e,label='dt=0.2',color='brown',s=11)

ax.set_title('x-t graf ovisno o koraku')
ax.set_xlabel('t[s]')
ax.set_ylabel('x[m]')

ax.legend()
plt.show()