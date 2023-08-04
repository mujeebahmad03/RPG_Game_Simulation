from game_entity import GameEntity

class Item(GameEntity):
    def __init__(self, name, x, y, value, item_type):
        super().__init__(name, x, y)
        self.value = value
        self.type = item_type