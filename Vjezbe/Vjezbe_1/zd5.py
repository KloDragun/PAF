import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Unos vrijednosti
x1=2
y1=1
x2=3
y2=5

#Pretpostavljamo da je x1 manje od x2, inace if statemente radit moramo
x=np.linspace(x1-3,x2+3,30)

#Matematicki dio
k=float((y2-y1)/(x2-x1))
var=[k,-k*x1+y1]
t=var[0]*x+var[1]
print("Varijable:")
print(var)
#Za markere
xk=[x1,x2]
yk=[y1,y2]


#Plottanje
plt.plot(x,t)
plt.scatter(xk,yk)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Zadatak 5")
plt.xticks()

#Save yes-no
save=input("Ako zelite save sliku napisite DA, inace ce se pokazati")
if save=='DA':
    name=input("Napiste ime datoteke")
    plt.savefig("{}.pdf".format(name), dpi=200)
else:
    plt.show()