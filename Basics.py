#Zakladni operace v Pythonu
a = 4 #promenna s nazvem a s hodnotou 4
b = 2 #promenna s nazvem b s hodnotou 2

scitani = a + b
odcitani = a - b
nasobeni = a * b
deleni = a // b
modulo = a % 3 #zbytek po deleni 3

#Funkce print() slouzi k vypsani vysledku uzivateli
print("Vysledky naseho pocitani:")#text (string) piseme vzdy v uvozovkach
print(scitani)
print(odcitani)
print(nasobeni)
print(deleni)
print(modulo)
print("\n") #Zde vypisujeme novou prazdnou radku

if a == 0:
    print ("Promenna a = 0")
elif a == 1:
    print ("Promenna a = 1")
elif a == 2:
    print ("Promenna a = 2")
elif a == 3:
    print ("Promenna a = 3")
else:
    print ("Promenna a = 4")