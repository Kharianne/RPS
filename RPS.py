import random #importuje knihovnu pro generovani a praci s nahodnymi cisly

player_choice = input("I choose:")


def name_to_number(name):
    if name == "rock":
        number = 0
        return number

    elif name == "paper":
        number = 1
        return number
    elif name == "scissors":
        number = 2
        return number
    else:
        return -1

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

def rps(player_choice):
    print ()
    print ("Player chooses:", player_choice)
    player_number = name_to_number(player_choice)

    #following if is for handling incorrect input
    if player_number == -1:
        print ("Incorrect input.")
    comp_number = random.randrange(0, 3)
    comp_choice = number_to_name(comp_number)
    print ("Computer chooses:", comp_choice)

    if comp_number == player_number:
        print ("Player and computer tie!")
    elif ((comp_number - player_number) % 3) == 1:
        print ("Computer wins!")
    else:
        print ("Player wins!")

rps(player_choice)
