from Snakes_ladders.Dice_Class import Dice  # Importing Dice Class from directory file
from Snakes_ladders.Player_Class import Player  # Importing Player Class from directory file

a = int(input("Enter number of players between 2-4: "))
# implement a way to catch ValueError if an integer is not input

# ensures that there can be minimum 2 players and maximum 4 players
while a < 2 or a > 4:
    a = int(input("That number is Invalid, please pick an integer from 2-4: "))

# used to store Player objects into the players list
count_players = 1

# creating an empty list to store objects of Player class
players = []

# creates objects of Player class and stores them in the players list
while count_players <= a:
    name = str(input(f'Enter name of player number {count_players}: '))
    obj = Player(name, 0)
    players.append(obj)
    obj.greet()
    count_players += 1

# creating object of class dice, this will control the dice rolling mechanism using the random library
Dice = Dice()

# creates a condition that becomes True when a player has won, important for terminating program
game_over = False

cont = input('Press enter to Continue')
print("-------------------------------------------------------------------")

# while loop continues the game as long as no players have won
while True:

    # inner for loop present to call needed class functions for each Player object stored in players list
    for player in players:
        roll = Dice.roll()
        player.move(roll)
        player.check_ladders()
        player.check_snakes()

        # if statement executes when function returns True if a player has won according to the rules
        if player.check_win():
            # updates boolean value to true if a player has won
            game_over = True
            break
        cont = input('Press enter to Continue')
        print("-------------------------------------------------------------------")

    # Checks if boolean value is true or not to keep continuing the game
    # Keeps running while loop if condition is not true
    if game_over:
        break