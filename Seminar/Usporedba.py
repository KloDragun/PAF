import Projectile as pr
import numpy as np
import matplotlib.pyplot as plt

#Unosimo varijable, trenje i masa su zadnje dvije varijable
t1=pr.Projectile(10,20,45,0,0.001,2.3,0.05,0.8,2)
t2=pr.Projectile(10,20,45,0,0.001,2.3,0.05,0.8,4)
t3=pr.Projectile(10,20,45,0,0.001,2.3,0.05,0.8,8)
t4=pr.Projectile(10,20,45,0,0.001,2.3,0.05,0.4,2)
t5=pr.Projectile(10,20,45,0,0.001,2.3,0.05,0.6,2)
t6=pr.Projectile(10,20,45,0,0.001,2.3,0.05,0.8,2)

#Uzimamo x i y arrayeve iz move-a
t1x,t1y=t1.RungeKutta_Move()
t2x,t2y=t2.RungeKutta_Move()
t3x,t3y=t3.RungeKutta_Move()
t4x,t4y=t4.RungeKutta_Move()
t5x,t5y=t5.RungeKutta_Move()
t6x,t6y=t6.RungeKutta_Move()

#Plottanje
plt.plot(t1x,t1y)
plt.plot(t2x,t2y)
plt.plot(t3x,t3y)
plt.legend(['m=2 kg', 'm=4 kg', 'm=8 kg'])
plt.title("x-y graf za različite mase kada je Cd=0.8")
plt.ylabel('y [m]')
plt.xlabel('x [m]')
plt.show()

print('Za isti Cd dometi su:{} {} {}'.format(t1x[-1],t2x[-1],t3x[-1]))
print('Razlika između zadnjeg i prvog dometa(isti Cd) je {}'.format(t3x[-1]-t1x[-1]))
plt.plot(t4x,t4y)
plt.plot(t5x,t5y)
plt.plot(t6x,t6y)
plt.ylabel('y [m]')
plt.xlabel('x [m]')
plt.legend(['Cd=0.4', 'Cd=0.6', 'Cd=0.8'])
plt.title("x-y graf za različita trenja kada je m=2 kg,")
plt.show()

print('Za istu masu dometi su:{} {} {}'.format(t4x[-1],t5x[-1],t6x[-1]))
print('Razlika između zadnjeg i prvog dometa(ista masa) je {}'.format(t6x[-1]-t4x[-1]))
