import numpy as np
#Pocetni parametar
h=0.01

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

    #Međe, lazy way
    medja=0
    for i in tocke:
        medja+=funk(i)*dx
    
    gornja_medja=medja-funk(tocke[0])*dx
    donja_medja=medja-funk(tocke[-1])*dx

    return donja_medja,gornja_medja

def trapezna(funk,donja_granica,gornja_granica,podjele):
    #Lista tocaka za integraciju+korak između točaka, kao i u pravokutnoj
    tocke=np.linspace(donja_granica,gornja_granica,podjele)
    dx=tocke[1]-tocke[0]

    #Suma
    suma=0
    i=1
    while i<(len(tocke)):
          suma+=(funk(tocke[i-1])+funk(tocke[i]))
          i+=1
    
    #Rezultat
    trapez=(dx/2)*suma
    return trapez
