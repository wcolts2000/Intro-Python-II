# Write a class to hold player information, e.g. what room they are in
# currently.
import sys


class Player(object):

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.is_playing = True

    def examine(self, obj):
        print(obj)

    # def search(self):
    #     print(self.location['secrets'])
