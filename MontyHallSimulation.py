# Remi LeBlanc
# Monty Hall Simulation

import random


def monty_hall(interactive=True, switch=None):
    """
    Runs a single monty hall problem, either interactive or not interactive version, based on parameters.
    The non interactive version takes an additional parameter to switch or stay on the simulation.

    :param interactive: Boolean. True = interactive version, False = random simulation
    :param switch: Boolean. For the non interactive version: switch = True, always switch. switch = False, always stay
    :return: Non interactive version returns True or False based on if correct door was selected (correct -> True)
    """

    doors = [False, False, False]  # false is a zonk
    car = random.randrange(3)  # randomly pick a door for car to be behind
    doors[car] = True  # car

    if interactive:
        # user picks a door
        while True:  # make sure user enters 1 2 or 3
            choice = input("Pick door 1, 2, or 3: ")
            if choice in {'1', '2', '3'}:
                break
        choice = int(choice) - 1  # for indexing
    else:  # Simulation
        # randomly choose a door
        choice = random.randrange(3)

    # calculate which door to reveal
    all_doors = {0, 1, 2}
    reveal = all_doors.difference({choice, car})  # set of doors not chosen and not with the car, could be one or two doors
    if len(reveal) > 1:  # if they chose the right door
        reveal = random.sample(reveal, 1)  # randomly choose to open one of the other two doors
    reveal = reveal.pop()  # get the door from the single item set

    # get the door other than their choice and one revealed, for the switch option
    other_door = all_doors.difference({choice, reveal}).pop()

    if interactive:
        print(f"Door {reveal+1} does not have the car.")
        while True:  # make sure user enters y or n
            switch = input(f"You have chosen door {choice+1}. Would you like to switch to door {other_door+1}? (y/n)")
            if switch == 'y':
                choice = other_door
                break
            elif switch == 'n':
                break

        # print the results of the game
        if doors[choice]:
            print(f"Door {choice+1} has the car! Congratulations!\n")
        else:
            print(f"Door {choice+1} is zonk. Door {car+1} had the car! Better luck next time!\n")

    else:  # not interactive
        if switch:  # parameter passed into function call
            choice = other_door  # switch first choice
        return doors[choice]  # True or False


def simulation(switch, n):
    """
    Calls monty_hall() n times either switching or staying every time, based on boolean parameter switch.

    :param switch: True = always switch. False = always stay.
    :param n: Number of times to run random simulation.
    :return: prints out the winning percentage from n simulations of the game
    """

    wins = 0
    for i in range(n):
        if monty_hall(False, switch):  # not interactive and switch based on parameter
            wins += 1

    winning_percent = round((wins/n)*100, 2)

    print(f"{['Switching' if switch else 'Staying'][0]} every time gave a winning percentage of {winning_percent}% after {n} random simulations.")


if __name__ == '__main__':
    while True:
        option = input("""
Monty Hall Game!
Enter 1 for interactive game
Enter 2 to simulate switching every time
Enter 3 to simulate staying every time
""")

        if option == '1':
            monty_hall()

        elif option in {'2', '3'}:  # Computer simulation
            # ask how many times user wants simulation ran
            while True:  # make sure user enters a number
                n = input("Enter the number of simulations you wish to run: ")
                try:
                    n = int(n)
                    break
                except ValueError:  # not a number, ask again
                    pass

            if option == '2':  # switch
                simulation(True, n)
            elif option == '3':  # stay
                simulation(False, n)
        else:  # user didn't enter an valid option, as again
            continue

        while True:  # make sure user enters y or n
            ans = input("Play again? (y/n)")
            if ans == 'y' or ans == 'n':
                break
        if ans == 'n':  # end game
            break

    print('Thanks for playing!')
