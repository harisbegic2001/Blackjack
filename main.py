import random as r

def sums(lists):
    broj = 0
    for i in range(len(lists)):
        broj += lists[i]
    
    return broj


lista_br = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    yes_no = input("Do you want to play a blackjack? Type 'y' or 'n': ").lower()
    lista_igrac = []
    lista_komp = []
    sum_player = 0
    sum_computer = 0

    if yes_no == "y":
        print("Igrate")

        for i in range(2):
            lista_igrac.append(lista_br[r.randint(0,len(lista_br)-1)])

            lista_komp.append(lista_br[r.randint(0,len(lista_br)-1)])
        
        print(f"Your cards: {lista_igrac}")

        print(f"Computers first card is: {lista_komp[0]}")

        new_card = input("Do you want another card? Type 'y' for yes and 'n' for no: ").lower()

        if new_card == "y":
            lista_igrac.append(lista_br[r.randint(0,len(lista_br)-1)])
        
        else:
            print("We will se if it is a good choice")
        
        sum_player = sums(lista_igrac)

        sum_computer = sums(lista_komp)

        if sum_player > 21:
            print("Bad choice, you lost")
            continue

        elif sum_player == sum_computer:
            print("It's a draw!!")
            continue
        
        elif sum_player > sum_computer:
            print("You WON!!")
            continue
        
        elif sum_player < sum_computer:
            print("You lost :( ")

    else:
        print("End of the game!")
        break