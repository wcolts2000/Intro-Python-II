# Implement a class to hold room information. This should have name and
# description attributes.


class Room(object):

    adjacent_rooms = {"e_to": '', "n_to": '', "s_to": '', "w_to": ''}

    treasures = []

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False
