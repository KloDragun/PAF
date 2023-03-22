
import numpy as np
import matplotlib.pyplot as plt
y=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #M
x=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #kut
umn=[]

#Umnozak x i y
for i in range(len(x)):
    umn.append(x[i]*y[i])

#Srednja vrijednost od xy
srednja=np.mean(umn)

#Kvadrat x
kvadratx=[]
for i in range(len(x)):
    kvadratx.append(x[i]*x[i])

#Kvadrat y
kvadraty=[]
for i in range(len(y)):
    kvadraty.append(y[i]*y[i])

#Koeficijent
a=srednja/np.mean(kvadratx)

#x-y osi
xos=np.linspace(0,1.2,100)
yos=a*xos

#Fittna f-ja (za reference)
z=np.polyfit(x,y,deg=1)
tos=z[0]*xos

#Devijacija
d=(1/len(x))*((np.mean(kvadraty)/np.mean(kvadratx))-a**2)
d=np.sqrt(d)

#Plottanje
plt.plot(xos,yos)
plt.plot(xos,tos)
plt.errorbar(x,y,d,linestyle='None', marker='')
plt.scatter(x,y)
plt.show()