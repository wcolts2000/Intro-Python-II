import cmd
import textwrap
import sys
import os
import time
import random

from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
my_player = Player('', room['outside'])


def main():
    # Make a new player object that is currently in the 'outside' room.
    title_screen()

    # if __name__ == '__main__':
    #     main()
    # Write a loop that:
    #


def print_location(my_player):
    # print(room['outside'])
    # print(room['foyer'])
    # print(room['overlook'])
    # print(room['narrow'])
    # print(room['treasure'])
    if my_player.location.name == "Outside Cave Entrance":
        print('You stand ' + my_player.location.name)
    else:
        print('You enter the ' + my_player.location.name)
    print(my_player.location.description)


def prompt():
    print('Input a command')
    action = input('> ')
    # acceptable_actions = ['move', 'go', 'travel', 'walk',
    #                       'quit', 'inspect', 'interact', 'look', 'examine']
    actionArr = action.split(' ')
    # while action.lower() not in acceptable_actions:
    #     print('Unknown action, try again.\n')
    #     action = input('> ')
    if len(actionArr) == 1:
        if action.lower() == 'quit' or action.lower() == 'q':
            sys.exit()
        elif action.lower() in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west', 'up', 'down', 'left', 'right']:
            player_move(action.lower())
    else:
        print('thats too many right now')
        # acceptable_actions = ['move', 'go', 'travel', 'walk',
        #                       'quit', 'inspect', 'interact', 'look', 'examine']
    # elif action.lower() in ['inspect', 'interact', 'look', 'examine']:
    #     self.player_examine(action.lower())


def player_move(direction):
    # ask = 'Where would you like to move to?\n'
    if direction in ['up', 'north', 'n']:
        if hasattr(my_player.location, 'n_to'):
            direction = my_player.location.n_to
            movement_handler(direction)
        else:
            print('\n' + 'There is nothing in that direction to move to')
            prompt()
    elif direction in ['left', 'west', 'w']:
        if hasattr(my_player.location, 'w_to'):
            direction = my_player.location.w_to
            movement_handler(direction)
        else:
            print('\n' + 'There is nothing in that direction to move to')
            prompt()
    elif direction in ['right', 'east', 'e']:
        if hasattr(my_player.location, 'e_to'):
            direction = my_player.location.e_to
            movement_handler(direction)
        else:
            print('\n' + 'There is nothing in that direction to move to')
            prompt()
    elif direction in ['down', 'south', 's']:
        if hasattr(my_player.location, 's_to'):
            direction = my_player.location.s_to
            movement_handler(direction)
        else:
            print('\n' + 'There is nothing in that direction to move to')
            prompt()


def movement_handler(destination):
    print(f'\n You have moved to the {destination.name}')
    my_player.location = destination
    print_location(my_player)


def main_game_loop():
    while my_player.is_playing:
        header()
        print_location(my_player)
        prompt()
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    if __name__ == '__main__':
        main_game_loop()
#
#  Terminal Output Helpers
#


def title_screen_selections():
    option = input('> ')
    if option.lower() == ('play'):
        setup_game()  # placeholder until written
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("please enter a valid command.")
        option - input('> ')
        if option.lower() == ('play'):
            setup_game()  # placeholder until written
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()


def header():
    os.system('clear')
    print('#############################################')
    print('#       Welcome to "Adventure Lurks"!       #')
    print('#############################################')


def title_screen():
    header()
    print('- Play - ')
    print('- Help - ')
    print('- Quit - ')
    title_screen_selections()


def help_menu():
    header()
    print('    - Use up, down, left, right to move -    ')
    print('    - Type commands to do them -             ')
    print('    - Use "examine" to inspect something -   ')
    print('    - Use "search" to look through a room -  ')
    print('    - Use "quit" to stop the game -          ')
    print('    - Good luck and have fun!!! -            ')
    title_screen_selections()


def setup_game():
    os.system('clear')

    ######## NAME COLLECTING ########
    question1 = 'Hello, what is your name?\n'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('> ')
    # my_player.name = player_name

    ######## INTRODUCTION ########
    speech1 = 'Welcome, ' + player_name + " to this fantasy world! \n"
    speech2 = "I hope it greets you well! \n"
    speech3 = "Just make sure you don't get too lost!!! \n"
    speech4 = "Muah ha ha ha ha......! \n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    main_game_loop()


main()
