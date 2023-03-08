def pravac(x1,y1,x2,y2):
    k=float((y2-y1)/(x2-x1))
    print("Jednadzba pravca kroz tocke ({},{}) i ({},{}) je:\n".format(x1,y1,x2,y2))
    if (-k*x1+y1)>0:
        print("y={}x+{}".format(k,-k*x1+y1))
    else:
        print("y={}x{}".format(k,-k*x1+y1))



#Unos vrijednosti
x1=2
y1=3
x2=6
y2=12


pravac(x1,y1,x2,y2)
