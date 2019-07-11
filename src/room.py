# Implement a class to hold room information. This should have name and
# description attributes.


class Room(object):

    def __init__(self, name, description, items, illuminated):
        self.name = name
        self.description = description
        self.completed = False
        self.items = items
        self.is_light = illuminated

    def __str__(self):
        str = f"""
              \n
              \n{self.name}
              \n{self.description}\n"""
        return str

    def get_items_list(self):
        return ", ".join([item.name for item in self.items])
