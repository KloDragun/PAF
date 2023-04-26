import calculus as cal
import numpy as np
import matplotlib.pyplot as plt

#Upisemo funkciju
def funkcija(x):
    return ((2*(x**2)) +3)

#Test za međe, maknuti # za test
x,y=cal.pravokutna(funkcija,1,14,35)
#print(x,y)

#Test za trapez, maknuti # za test
t=cal.trapezna(funkcija,1,14,35)
#print(t)

#Plottanje grafa za provjeru
koraci=np.linspace(10,1000,100)

lista_pravokutni=[]
lista_trapezni=[]
for i in koraci:
    lista_pravokutni.append(cal.pravokutna(funkcija,0,1,int(i)))
    lista_trapezni.append(cal.trapezna(funkcija,0,1,int(i)))
print(lista_pravokutni)
gornji=[]
donji=[]
for i in range(len(lista_pravokutni)):
    donji.append(lista_pravokutni[i][0])
    gornji.append(lista_pravokutni[i][1])

analiticko=[]
for i in koraci:
    analiticko.append(11/3)
fig, ax = plt.subplots(figsize=(12,12))

ax.plot(koraci,analiticko, linewidth=2,color='red',label='Analiticki')
ax.scatter(koraci,gornji,label='Gornje Međe',s=11)
ax.scatter(koraci,donji,label='Donje Međe',s=11)
ax.scatter(koraci,lista_trapezni,label='Trapezna',color='purple',s=11)

ax.set_title('Intergracija f-je ovisno o koracima')
ax.set_xlabel('Broj koraka')
ax.set_ylabel('f(x)')

ax.legend()
plt.show()

