import particle as par
import matplotlib.pyplot as plt

#Napomena!! Ovo je ujedino i 2. zd


#Liste za devijaciju vrijeme
dev=[]
dt=[0]

#While petlja za korak
while dt[-1]<=0.2:
    dt.append(dt[-1]+0.01)
    t1=par.Particle(10,60,0,0,dt[-1])
    dev.append(abs(t1.analiticko()-t1.range())/t1.analiticko()*100)
del dt[0]

#Plottanje
plt.plot(dt,dev)
plt.title("Postotak greske-korak graf")
plt.xlabel("Korak dt [s]")
plt.ylabel("Absolutna greska [%]")
plt.show()

#Sličnost numeričkog i analitičkog rješenja ovisi o koraku dt, što je on veći, veća pogreška