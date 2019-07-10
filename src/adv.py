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
    'outside':  Room("Outside The Cave Entrance",
                     "North of you, the cave mouth beckons", ['lamp', 'oil', 'key', 'rock']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
    os.system('clear')
    title_screen()

    # if __name__ == '__main__':
    #     main()
    # Write a loop that:
    #


def print_location():
    if my_player.current_room.name == "Outside The Cave Entrance":
        print('You stand ' + my_player.current_room.name)
    else:
        print('You enter the ' + my_player.current_room.name)
    print(my_player.current_room.description)


def print_room_items():
    if len(my_player.current_room.items) == 0:
        print('There is nothing here worth noting.')
    else:
        items = ''
        for item in my_player.current_room.items:
            items += item + " "
        print('In this area you can see ' + items)


def prompt(my_player):
    print('\n' + 'What would you like to do?')
    action = input('> ')
    # acceptable_actions = ['move', 'go', 'travel', 'walk',
    print_room_items()
    #                       'quit', 'inspect', 'interact', 'look', 'examine']
    actionArr = action.split(' ')
    # while action.lower() not in acceptable_actions:
    #     print('Unknown action, try again.\n')
    #     action = input('> ')
    if len(actionArr) == 1:
        if action.lower() in ['quit', 'q']:
            os.system('clear')
            sys.exit()
        elif action.lower() == ['ex', 'examine']:
            # print_room_items(my_player)
            print_room_items()
        elif action.lower() in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west', 'up', 'down', 'left', 'right']:
            os.system('clear')
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
        if hasattr(my_player.current_room, 'n_to'):
            direction = my_player.current_room.n_to
            movement_handler(direction)
        else:
            print('\n' + 'There is nothing in that direction to move to')
            prompt(my_player)
    elif direction in ['left', 'west', 'w']:
        if hasattr(my_player.current_room, 'w_to'):
            direction = my_player.current_room.w_to
            movement_handler(direction)
        else:
            print('\n' + 'There is nothing in that direction to move to')
            prompt(my_player)
    elif direction in ['right', 'east', 'e']:
        if hasattr(my_player.current_room, 'e_to'):
            direction = my_player.current_room.e_to
            movement_handler(direction)
        else:
            print('\n' + 'There is nothing in that direction to move to')
            prompt(my_player)
    elif direction in ['down', 'south', 's']:
        if hasattr(my_player.current_room, 's_to'):
            direction = my_player.current_room.s_to
            movement_handler(direction)
        else:
            print('\n' + 'There is nothing in that direction to move to')
            prompt(my_player)


def movement_handler(destination):
    print(f'\n You have moved to the {destination.name}')
    my_player.current_room = destination
    os.system('clear')
    header()
    print_location()


def main_game_loop(player_name):
    my_player.name = player_name
    while my_player.is_playing:
        prompt(my_player)
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    if __name__ == '__main__':
        main_game_loop(player_name)


#######################################
#  Terminal Output Helpers
#######################################


def title_screen_selections():
    option = input('> ')
    if option.lower() in ['play', 'p']:
        os.system('clear')
        setup_game()
    elif option.lower() in ['help', 'h']:
        os.system('clear')
        help_menu()
    elif option.lower() in ['quit', 'q']:
        os.system('clear')
        sys.exit()
    while option.lower() not in ['play', 'p', 'help', 'h', 'quit', 'q']:
        os.system('clear')
        print("please enter a valid command.")
        title_screen_selections()


def header():
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
    print('  - Type "play" or "p" to start the game -    ')
    print('  - Use "n", "s", "e", "w" to move -          ')
    print('  - Use "examine" or "ex" to inspect surroundings -   ')
    print('  - Use "quit" or "q" to stop the game -      ')
    print('  - Type 2 commands to interact -             ')
    print('  - Good luck and have fun!!! -               ')
    print('  - Play - Help - Quit - ')
    title_screen_selections()


#######################################
#  GAME SETUP
#######################################

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
    os.system('clear')
    header()
    print_location()
    main_game_loop(player_name)


main()
