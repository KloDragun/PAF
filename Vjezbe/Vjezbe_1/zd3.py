
def unos():
    while(1):
        tocka=[input("Upisite koordinatu x za tocku"),input("Upisite koordinatu y za tocku")]
        c1=0
        test=[tocka[0].replace('.','',1).replace('-','',1),tocka[1].replace('.','',1).replace('-','',1)]
        if test[0].isdigit()==True and test[1].isdigit()==True:
            c1=1
            break
        else:
            print("Upisite ponovo koordinate tocke")
    return tocka


print("Upisite koordinate za tocku 1")
tocka1=unos()
print("Upisite koordinate za tocku 2")
tocka2=unos()

x1=float(tocka1[0])
y1=float(tocka1[1])
x2=float(tocka2[0])
y2=float(tocka2[1])

k=float((y2-y1)/(x2-x1))
print(k)

print("Jednadzba pravca kroz tocke {} i {} je:\n".format(tocka1,tocka2))
if (-k*x1+y1)>0:
    print("y={}x+{}".format(k,-k*x1+y1))
else:
    print("y={}x{}".format(k,-k*x1+y1))



