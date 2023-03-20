#Broj iteracija
N=[200,2000,20000]


#Zbrajanje
suma=[0,0,0]
for j in range(len(N)):
    for i in range(N[j]):
        suma[j]=suma[j]+ 1/3

print(suma)

#Oduzimanje
rez=[5,5,5]
for j in range(len(N)):
    for i in range(N[j]):
        rez[j]=rez[j]- 1/3

print(rez)

#Vidimo što više iteracija radimo, to su pogreške na većoj decimali, što je logično jer se puno malih pogrešaka u aproksimaciji zbraja(S lijeva na desno svakoj listi)