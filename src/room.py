# Implement a class to hold room information. This should have name and
# description attributes.


class Room(object):

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.completed = False
        self.items = items
