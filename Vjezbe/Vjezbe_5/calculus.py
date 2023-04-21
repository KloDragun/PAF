import numpy as np
#Pocetni parametar
h=0.01

#Zeljena funkcija, testno
def funkcija(x):
    return x**3

#1. Metoda, malo weird jer trazi da primimo citavu f-ju a 2. metoda ne trazi
def derivacija(funk,tocka,ts):
    if ts=='y':
        return (funk(tocka+h)-funk(tocka))/h
    elif ts=='n':
        return (funk(tocka+h)-funk(tocka-h))/(2*h)
    else:
        print("Probajte ponovo")

#2. Metoda
def granica(donja,gornja,korak,ts):
    tocke=np.arange(donja,gornja+korak,korak)
    derivacije=[]
    if ts=='y':
        for i in tocke:
            derivacije.append((funkcija(i+korak)-funkcija(i))/korak)
    elif ts=='n':
        for i in tocke:
            derivacije.append((funkcija(i+korak)-funkcija(i-korak))/(2*korak))
    else:
        print("Probajte ponovo")
    print(derivacije)