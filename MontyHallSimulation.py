# Remi LeBlanc
# Monty Hall Simulation

import random


def monty_hall(interactive=True, switch=None):
    doors = [False, False, False]  # false is a zonk
    car = random.randrange(3)
    doors[car] = True  # car

    if interactive:
        while True:  # make sure user enters 1 2 or 3
            choice = input("Pick door 1, 2, or 3: ")
            if choice in {'1', '2', '3'}:
                break
        choice = int(choice) - 1  # for indexing
    else:
        choice = random.randrange(3)

    a = {0, 1, 2}
    b = {choice, car}
    reveal = a.difference(b)  # set of doors not chosen and not with the car, could be two doors
    if len(reveal) > 1:
        reveal = random.sample(reveal, 1)  # if they chose the right door, randomly choose to open one of the others
    reveal = reveal.pop()  # get the door from the single item set
    c = {choice, reveal}
    other = a.difference(c).pop()  # gets the door other than their choice and one revealed

    if interactive:
        print(f"Door {reveal+1} does not have the car.")
        while True:  # make sure user enters y or n
            switch = input(f"You have chosen door {choice+1}. Would you like to switch to door {other+1}? (y/n)")
            if switch == 'y':
                choice = other
                break
            elif switch == 'n':
                break
        if doors[choice]:
            print(f"Door {choice+1} has the car! Congratulations!\n")
        else:
            print(f"Door {choice+1} is zonk. Door {car+1} had the car! Better luck next time!\n")

    else:  # not interactive
        if switch:
            choice = other  # switch choice
            return doors[choice]
        else:
            return doors[choice]


def simulation(switch):
    wins = 0

    while True:  # make sure user enters a number
        n = input("Enter the number of simulations you wish to run: ")
        try:
            n = int(n)
            break
        except ValueError:
            pass


    for i in range(n):
        if monty_hall(False, switch):  # not interactive and switch based on arg
            wins += 1

    winning_percent = round((wins/n)*100, 2)
    if switch:
        action = "Switching"
    else:
        action = "Staying"
    print(f"{action} every time gave a winning percentage of {winning_percent}%")


if __name__ == '__main__':
    while True:
        option = input("""
Monty Hall Game!
Press 1 for interactive game
Press 2 to simulate switching every time
Press 3 to simulate staying every time
""")

        if option == '1':
            monty_hall()
        elif option == '2':
            simulation(switch=True)
        elif option == '3':
            simulation(switch=False)

        while True:  # make sure user enters y or n
            ans = input("Play again? (y/n)")
            if ans == 'y' or ans == 'n':
                break
        if ans == 'n':
             break

    print('Thanks for playing!')
