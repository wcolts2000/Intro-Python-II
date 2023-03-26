class Item():

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")


class Lightsource(Item):

    def __init__(self, name, description):
        super().__init__(name, description)

    def on_take(self):
        super().on_take()

    def on_drop(self):
        print(f"It's not wise to drop your source of light!")
        print(f"You have dropped {self.name}")
