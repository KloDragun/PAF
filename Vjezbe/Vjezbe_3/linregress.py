
import numpy as np
import matplotlib.pyplot as plt
y=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #M
x=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #kut
zbroj=[]

#Zbroj x i y
for i in range(len(x)):
    zbroj.append(x[i]+y[i])

#Srednja vrijednost od xy
srednja=np.mean(zbroj)/len(zbroj)

#Srednja vrijednost od x
srednjax=np.mean(x)

#Srednja vrijednost od y
srednjay=np.mean(y)

#koeficijent
a=srednja/(srednjax**2)

#x-y osi
xos=np.linspace(0,1.2,100)
yos=a*xos

#Fittna f-ja (za reference)
z=np.polyfit(x,y,deg=1)
tos=z[0]*xos

#Devijacija
d=abs((1/len(x))*(((srednjay**2)/(srednjax**2))-a**2))
d=np.sqrt(d)
print(d)

#Plottanje
plt.plot(xos,yos)
plt.plot(xos,tos)
plt.errorbar(x,y,d,linestyle='None', marker='')
plt.scatter(x,y)
plt.show()