import random #importuje knihovnu pro generovani a praci s nahodnymi cisly

player_choice = input("I choose:") #funkce input precte od uzivatele vstup

#Funkce name_to_number prevadi text na cislo
#podle zadanych parametru
def name_to_number(name):
    if name == "rock": #slovu rock priradi cislo 0
        number = 0
        return number

    elif name == "paper": #slovu paper priradi cislo 1
        number = 1
        return number
    elif name == "scissors": #slovu scissors pripradi cislo 2
        number = 2
        return number
    else:
        return -1 #vraci tuto hodnotu, pokud neni vstup validni

#Funkce number_to_name prevadi cislo na text,
#prevodni princip funguje naprosto stejnej
#jako u predchazejici funkce
def number_to_name(number):
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "paper"
        return name
    elif number == 2:
        name = "scissors"
        return name
    else:
        return "Given number is incorrect"

#Samotna logika hry
#Dochazi volani vyse nadefinovanych funkci
#Vypsani volby hrace a pocitace
#Samotne urceni vyherce
def rps(player_choice):
    print ()#odradkovani
    print ("Player chooses:", player_choice) #jednoducha funkce print = zde vypise volbu hrace
    player_number = name_to_number(player_choice)#zde volame funkci name_to_number, abychom prevedli
                                                 #text (vstup od uzivatele) na cislo


    if player_number == -1: #tato podminka odchytava pripady nevalidniho vstupu
        print ("Incorrect input.") #zde dojde k vypsani chybove hlasky

    comp_number = random.randrange(0, 3) #funkce randrange slouzi pro generovani nahodnych cisel
                                         #pri zadanych argumentech (0,3) generuje nahodne cisla: 0 1 2
    comp_choice = number_to_name(comp_number)#zavolani teto funkce prevede vygenerovane cislo z
                                             # predchoziho kroku na text
    print ("Computer chooses:", comp_choice) #zde vypisujeme jakou moznost zvolil pocitac

#Nasleduje urceni viteze na zaklade naseho algoritmu
    if comp_number == player_number:
        print ("Player and computer tie!")
    elif ((comp_number - player_number) % 3) == 1:
        print ("Computer wins!")
    else:
        print ("Player wins!")

#Zde zavolame nasi funkci
rps(player_choice)
