from sys import stdout, exit
from os import system, name
from time import sleep
import random

from room import Room
from player import Player
from item import Item, Lightsource
from splash_screen import generate_screen, help_menu, title_screen, grave, header


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Declare all the items

items = {
    'lamp': Lightsource('lamp', 'an oil lamp with a wick still intact'),
    'oil': Item('oil', 'a vial of lamp oil'),
    'key': Item('key', 'a rusty key'),
    'rock': Item('rock', 'an oddly shaped rock...Perhaps it was chisseled to fit something.'),
    'parchment': Item('parchment', 'An old weathered piece of parchment, looks as though it may have once had something on it'),
    'basket': Item('basket', 'A precariously placed basket...wait!!! Did it just move a little?'),
    'antivenom': Item('antivenom', 'a vial of antivenom'),
    'cover': Item('cover', 'There appears to be a loose stone in the wall covering something'),
}


# Declare all the rooms

room = {
    'outside':  Room("Outside The Cave Entrance",
                     "North of you, the cave mouth beckons", [], True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [], True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [], False),
}


# Link items to rooms

room['outside'].items = [items['key'],
                         items['lamp'], items['rock'], items['oil']]
room['foyer'].items = [items['parchment']]
room['narrow'].items = [items['basket']]
room['treasure'].items = [items['antivenom'], items['cover']]

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
    # system('clear')
    clear()
    title_screen(setup_game)

    if __name__ == '__main__':
        main()


def main_game_loop(player_name):
    my_player.name = player_name
    while my_player.is_playing:
        prompt(my_player)
    grave(my_player.name, my_player.inventory)
    print("Game Over! Goodbye..." + '\n')
    exit()


def print_location(is_lit):
    if is_lit:
        if my_player.current_room.name == "Outside The Cave Entrance":
            print('You stand ' + my_player.current_room.name + '\n')
        else:
            print('You enter the ' + my_player.current_room.name + '\n')
        print(f'    > {my_player.current_room.description}' + '\n')
        print_room_items()
    else:
        print("It's pitch black in here!")


def print_room_items():
    if len(my_player.current_room.items) == 0:
        print('There is nothing here worth noting.')
    else:
        room_items = ''
        for item in my_player.current_room.items:
            room_items += item.name + ", "
        print('In this area you can see: ' + '\n' + f'      {room_items[:-2]}')


def prompt(my_player):
    print('\n' + 'What would you like to do?')

    action = input('> ')
    actionArr = action.split(' ')

    if len(actionArr) == 1:
        if action.lower() in ['quit', 'q']:
            # system('clear')
            clear()
            exit()
        elif action.lower() in ['gear', 'g', 'i', 'inventory']:
            my_player.check_gear()
        elif action.lower() in ['ex', 'examine']:
            if my_player.current_room.is_light:
                print_room_items()
            else:
                print("With no light, you can't see anything in here...")
        elif action.lower() in ['n', 's', 'e', 'w', 'north', 'south', 'east', 'west', 'up', 'down', 'left', 'right']:
            my_player.player_move(action.lower(), screen_generator_helper)
    elif len(actionArr) == 2:
        if actionArr[0].lower() in ['get', 'take', 'grab', 'steal']:
            take_item(actionArr[1])
        elif actionArr[0].lower() in ['drop', 'remove', 'throw', 'steal']:
            if actionArr[1].lower() == 'lamp':
                room['narrow'].is_light = False
                room['treasure'].is_light = False
            drop_item(actionArr[1])
    else:
        print('thats too many right now')


def take_item(item):
    item_present = False
    for i in my_player.current_room.items:
        if i.name == item:
            my_player.inventory.append(items[item])
            items[item].on_take()
            my_player.current_room.items.remove(items[item])
            item_present = True
    if not item_present:
        print('There is nothing by that name in this location')


def drop_item(item):
    my_player.current_room.items.append(items[item])
    items[item].on_drop()
    my_player.inventory.remove(items[item])


def screen_generator_helper(destination):
    my_player.current_room = destination
    # system('clear')
    clear()
    header()

    room_lit = False

    if my_player.current_room.is_light:
        room_lit = True
    if len(my_player.current_room.items):
        for i in my_player.current_room.items:
            if isinstance(i, Lightsource):
                room_lit = True
    if len(my_player.inventory):
        for i in my_player.inventory:
            if isinstance(i, Lightsource):
                room_lit = True
    if room_lit:
        generate_screen(my_player.current_room.name)
    else:
        generate_screen('Pitch Black')
    print_location(room_lit)


#######################################
#  GAME SETUP
#######################################

def setup_game():
    # system('clear')
    clear()
    header()

    ######## NAME COLLECTING ########
    question1 = 'Hello, what is your name?\n'
    for character in question1:
        stdout.write(character)
        stdout.flush()
        sleep(0.05)
    player_name = input('> ')

    ######## INTRODUCTION ########
    speech1 = 'Welcome, ' + player_name + " to this fantasy world! \n"
    speech2 = "I hope it greets you well! \n"
    speech3 = "Just make sure you don't get too lost!!! \n"
    speech4 = "Muah ha ha ha ha......! \n"
    for character in speech1:
        stdout.write(character)
        stdout.flush()
        sleep(0.03)
    for character in speech2:
        stdout.write(character)
        stdout.flush()
        sleep(0.03)
    for character in speech3:
        stdout.write(character)
        stdout.flush()
        sleep(0.1)
    for character in speech4:
        stdout.write(character)
        stdout.flush()
        sleep(0.2)
    # system('clear')
    clear()
    header()
    generate_screen('Outside The Cave Entrance')
    print_location(True)
    main_game_loop(player_name)


main()
