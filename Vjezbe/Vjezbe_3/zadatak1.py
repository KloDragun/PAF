#a)
a=5.0
b=4.935
print(a-b)

if((a-b) == 0.065):
    print("Ocekivano")
else:
    print("Neocekivano")
#Ocekujemo 0.065, ali dobijamo aproksimaciju broja 0.065 jer računala rade sa binarnim zapisima brojeva pa nemogu većinu decimalnih ostataka dobro zapisat(osim potencija broja 2), pa daju priblizne aproksimacije ostataka, s tim da do određene decimale dobijemo tocan rezultat jer python zaokruzi vrijednosti.

#b)
a=0.1
b=0.2
c=0.3

print(a+b+c)
if((a+b+c) == 0.6):
    print("Isti su")
else:
    print("Razliciti su")

#Dobili smo rezultat koji nije jednak 0.6 jer brojevi 0.1,0.2,0.3 se konvertiraju u binarni zapis koji zbog već navedenog nemože točno decimale prikazati nego aproksimacije, pa ni rezultat nije točan, već aproksimacija. (Napomena: svi brojevi su u PC-u binarni jer PC moze koristiti samo binarne vrijednosti, tako da kada napisemo float vrijednost tipa a=0.1 to je biti binarni zapis koji je u biti puno duži, ali smo ga mi zaokružili na neku vrijednost tako da tehnički nema konverzije)
