import numpy as np
#Pocetni parametar
h=0.01

#Zeljena funkcija, testno
def funkcija(x):
    return np.sin(x)

#1. Metoda, malo weird jer trazi da primimo citavu f-ju a 2. metoda ne trazi
def derivacija(funk,tocka,ts=0):
    if ts=='y':
        return (funk(tocka+h)-funk(tocka))/h
    else:
        return (funk(tocka+h)-funk(tocka-h))/(2*h)

#2. Metoda
def granica(donja,gornja,korak,ts=0):
    tocke=np.arange(donja,gornja+korak,korak)
    derivacije=[]
    if ts=='y':
        for i in tocke:
            derivacije.append((funkcija(i+korak)-funkcija(i))/korak)
    else:
        for i in tocke:
            derivacije.append((funkcija(i+korak)-funkcija(i-korak))/(2*korak))
    return tocke,derivacije

