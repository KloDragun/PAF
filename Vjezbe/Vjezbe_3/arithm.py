import numpy as np

#Par tocaka, znamo da je aritmeticka 1.5
tocke=np.linspace(1.4,1.6,10)

#Racunjanje sredine
sredina=0
for i in range(len(tocke)):
    sredina=sredina+tocke[i]

sredina=sredina/len(tocke)


devijacija=0
for i in range(len(tocke)):
    devijacija=devijacija+(tocke[i]-sredina)**2

devijacija=devijacija/(len(tocke)*(len(tocke)-1))

devijacija=np.sqrt(devijacija)
print(sredina)
print(devijacija)

