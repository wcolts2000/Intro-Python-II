# Write a class to hold player information, e.g. what room they are in
# currently.


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
            print('\n' + item.name + '\n')

    def print_inventory(self):
        print("You are carrying:\n  " +
              ", ".join([item.name for item in self.inventory]) + "\n")

    def no_access(self):
        print('\n' + 'There is nothing in that direction to move to')

    def player_move(self, direction, movement_handler):
        if direction in ['up', 'north', 'n']:
            if hasattr(self.current_room, 'n_to'):
                direction = self.current_room.n_to
                movement_handler(direction)
            else:
                self.no_access()
        elif direction in ['left', 'west', 'w']:
            if hasattr(self.current_room, 'w_to'):
                direction = self.current_room.w_to
                movement_handler(direction)
            else:
                self.no_access()
        elif direction in ['right', 'east', 'e']:
            if hasattr(self.current_room, 'e_to'):
                direction = self.current_room.e_to
                movement_handler(direction)
            else:
                self.no_access()
        elif direction in ['down', 'south', 's']:
            if hasattr(self.current_room, 's_to'):
                direction = self.current_room.s_to
                movement_handler(direction)
            else:
                self.no_access()
