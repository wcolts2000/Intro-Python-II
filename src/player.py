# Write a class to hold player information, e.g. what room they are in
# currently.
import sys


class Player(object):

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.is_playing = True
        self.inventory = []

    def inspect(self, item):
        print(item.description)

    def check_gear(self):
        for item in self.inventory:
            print(item.name)
