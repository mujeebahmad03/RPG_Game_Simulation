class GameEntity:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y +=dy