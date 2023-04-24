import numpy as np
import calculus as cal
import matplotlib.pyplot as plt




#Za testiranje
x,y=cal.granica(0,10,0.01)
t,z=cal.granica(0,10,0.1)
o,i=cal.granica(0,10,0.3)
test=[]
for i in x:
    test.append(np.cos(i))

#Plottanje
plt.plot(x,y)
plt.plot(t,z)
plt.plot(o,i)
plt.plot(x,test)
plt.show()


