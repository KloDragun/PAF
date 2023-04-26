import numpy as np
import calculus as cal
import matplotlib.pyplot as plt

#Upisemo funkciju
def funkcija(x):
    return np.sin(x)

#Za testiranje
x,y=cal.granica(funkcija,0,10,0.03)
t,z=cal.granica(funkcija,0,10,0.8)
k,l=cal.granica(funkcija,0,10,2)
test=[]
for i in x:
    test.append(np.cos(i))

#Plottanje
fig, ax = plt.subplots(figsize=(12,4))

ax.plot(x,test, linestyle='--', linewidth=3,label='Analiticki')
ax.plot(x,y,markersize=5,color='green' ,label='Korak: 0.03')
ax.plot(t,z,markersize=2,color='blue' ,label='Korak: 0.8')
ax.plot(k,l,markersize=4,color='orange' ,label='Korak: 2')

ax.set_title('Derivacija funkcije ovisno o koracima')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.legend()
plt.show()
