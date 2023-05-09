import harmonic_oscillator as har
import numpy as np
import matplotlib.pyplot as plt



m=3
k=1


#Rastuci
test1=har.HarmonicOscillator(m,k,2,3,0.001,10)
a,t1=test1.period()
test2=har.HarmonicOscillator(m,k,2,3,0.01,10)
b,t2=test2.period()
test3=har.HarmonicOscillator(m,k,2,3,0.05,10)
c,t3=test3.period()
test4=har.HarmonicOscillator(m,k,2,3,0.1,10)
d,t4=test4.period()
test5=har.HarmonicOscillator(m,k,2,3,0.25,10)
e,t5=test5.period()
test6=har.HarmonicOscillator(m,k,2,3,0.3,10)
f,t6=test6.period()
test7=har.HarmonicOscillator(m,k,2,3,0.4,10)
g,t7=test7.period()

#Dodatni
test8=har.HarmonicOscillator(m,k,2,3,0.04,10)
h,t8=test8.period()
test9=har.HarmonicOscillator(m,k,2,3,0.08,10)
l,t9=test9.period()
test10=har.HarmonicOscillator(m,k,2,3,0.15,10)
j,t10=test10.period()



#Određivanje perioda
w=np.sqrt(test1.k/test1.m)
T=(2*np.pi/w)
test=[]
testmat=[]
for i in test1.t:
    if i<=0.4:
        test.append(i)
        testmat.append(T)

#Plottanje
fig, ax = plt.subplots(figsize=(12,12))

ax.plot(test,testmat, linewidth=2,color='red',label='Analiticki')
ax.scatter(0.001,a,label='dt=0.001',s=11)
ax.scatter(0.01,b,label='dt=0.01',s=11)
ax.scatter(0.04,h,label='dt=0.04',s=11)
ax.scatter(0.05,c,label='dt=0.05',s=11)
ax.scatter(0.08,l,label='dt=0.08',s=11)
ax.scatter(0.1,d,label='dt=0.1',s=11)
ax.scatter(0.15,j,label='dt=0.15',s=11)
ax.scatter(0.3,f,label='dt=0.3',s=11)
ax.scatter(0.25,e,label='dt=0.25',s=11)
ax.scatter(0.4,g,label='dt=0.4',s=11)

ax.set_title('Graf perioda ovisno o koraku')
ax.set_xlabel('Iznos koraka [s]')
ax.set_ylabel('Udaljenost od analitickog t[s]')

ax.legend()
plt.show()