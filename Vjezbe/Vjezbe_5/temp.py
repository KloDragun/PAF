import numpy as np

def funkcija(x):
    return x**2

def integration(f, a, b, n):
    lista = np.linspace(a, b, n); donji_int = 0; gornji_int = 0
    dx = lista[1]-a
    for x in range(len(lista)-1):
        donji_int += f(lista[x])*abs(dx); gornji_int += f(lista[x+1])*abs(dx)
    return donji_int, gornji_int

def trapezoidal_integration(f, a, b, n):
    lista = np.linspace(a, b, n); integral = 0
    dx = lista[1]-a
    for x in range(len(lista)-1):
        integral += (f(lista[x])+f(lista[x+1]))*abs(dx)/2
    return integral

x=trapezoidal_integration(funkcija,23,35,543)
print(x)