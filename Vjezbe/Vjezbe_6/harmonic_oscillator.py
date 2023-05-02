import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:

    #Inicijalizacija
    def __init__(osc,masa,konstanta,pocetna_brzina,pocetni_polozaj,korak,stop):
        osc.m=masa
        osc.k=konstanta
        osc.x=[pocetni_polozaj]
        osc.v=[pocetna_brzina]
        osc.a=[-((osc.k*osc.x[0])/osc.m)]
        osc.t=[0]
        osc.dt=korak
        osc.stop=stop
    #Stvaranje lista
    def move(osc):
        while osc.t[-1]<osc.stop:
            osc.v.append(osc.v[-1]+osc.a[-1]*osc.dt)
            osc.x.append(osc.x[-1]+osc.v[-1]*osc.dt)
            osc.a.append(-(osc.k*osc.x[-1])/osc.m)
            osc.t.append(osc.t[-1]+osc.dt)

        del osc.t[-1]
        del osc.v[-1]
        del osc.x[-1]
        del osc.a[-1]

    #Grafovi
    def print(osc):
        osc.move()
        fig, axes = plt.subplots(1, 3, figsize=(100,4))
        axes[0].plot(osc.t,osc.x, linewidth=2,color='red',label='x-t graf')
        axes[1].plot(osc.t,osc.v, linewidth=2,color='blue',label='v-t graf')
        axes[2].plot(osc.t,osc.a, linewidth=2,color='green',label='a-t graf')
        plt.show()
      