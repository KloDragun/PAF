import numpy as np

#Par tocaka, znamo da je aritmeticka 1.5
tocke=np.linspace(3,4.11,10)

#Računanje sredine
sredina=0
for i in range(len(tocke)):
    sredina=sredina+tocke[i]

sredina=sredina/len(tocke)

#Računanje derivacije
devijacija=0
for i in range(len(tocke)):
    devijacija=devijacija+((tocke[i]-sredina)**2)

devijacija=devijacija/(len(tocke)*(len(tocke)-1))

devijacija=np.sqrt(devijacija)


#Printanje
print("Srednja vrijednost je {}".format(sredina))
print("Devijacija je {}".format(devijacija))
