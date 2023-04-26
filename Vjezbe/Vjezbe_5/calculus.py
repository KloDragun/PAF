import numpy as np
#Pocetni parametar
h=0.01

#f-ja za debug
def funkcija(x):
    return x**2

#1. Metoda
def derivacija(funk,tocka,ts=0):
    if ts=='y':
        return (funk(tocka+h)-funk(tocka))/h
    else:
        return (funk(tocka+h)-funk(tocka-h))/(2*h)

#2. Metoda
def granica(funk,donja,gornja,korak,ts=0):
    tocke=np.arange(donja,gornja+korak,korak)
    derivacije=[]
    if ts=='y':
        for i in tocke:
            derivacije.append((funk(i+korak)-funk(i))/korak)
    else:
        for i in tocke:
            derivacije.append((funk(i+korak)-funk(i-korak))/(2*korak))
    return tocke,derivacije

#3. Metoda 
def pravokutna(funk,donja_granica,gornja_granica,podjele):
    #Lista tocaka za integraciju+korak između točaka
    tocke=np.linspace(donja_granica,gornja_granica,podjele)
    dx=tocke[1]-tocke[0]

    gornja_medja=0
    for i in tocke:
        gornja_medja+=funk(i)*dx
    gornja_medja=gornja_medja-funk(tocke[0])

    donja_medja=0
    for i in tocke:
        donja_medja+=funk(i)*dx
    donja_medja=donja_medja-funk(tocke[-1])
    print(gornja_medja)
    print(donja_medja)

pravokutna(funkcija,1,4,100)