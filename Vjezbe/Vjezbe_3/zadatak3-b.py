import numpy as np

#Tocke inicijaliziramo
tocke=np.linspace(3,4.11,10)

#Srednja vrijednost
a=np.mean(tocke)

#Devijacija, kao np.std ali moramo podijelit s korijenom duljine -1 jer je std /N a nama treba N*N-1
b=np.std(tocke)*(1/np.sqrt(len(tocke)-1))

#Printanje
print("Srednja vrijednost je {}".format(a))
print("Devijacija je {}".format(b))