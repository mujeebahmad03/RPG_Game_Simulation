import random
from game_entity import GameEntity
from item import Item

class Player(GameEntity):
    defense_use_left = 3

    def __init__(self, name, x, y, health, damage):
        super().__init__(name, x, y)
        self.health = health
        self.base_damage = damage
        self.attack_boost = 0
        self.defense_boost = 0

    def move(self, dx, dy):
        super().move(dx, dy)

    def attack(self, enemy):
        if enemy.health > 0:
            attack_value = random.randint(self.base_damage + self.attack_boost - 5, self.base_damage + self.attack_boost)
            enemy.health -= attack_value
            print(f"{self.name} dealt {attack_value} damage on {enemy.name} . \n{enemy.name}'s health is: {enemy.health}")

    def use_item(self, item):
        if item.type == 'health' and self.health < 100:
            self.health += item.value
            self.health = min(self.health, 100)
            print(f"{self.name} used {item.name} and gained {item.value} health. \n{self.name}'s health has been restored to: {self.health}")
        elif item.type == 'attack':
            self.attack_boost += item.value
            print(f"{self.name} used {item.name} and gained {item.value} attack power.")
        elif item.type == 'defense' and Player.defense_use_left > 0:
            self.defense_boost += item.value
            Player.defense_use_left -= 1
            print(f"{self.name} used {item.name} and gained {item.value} defense power.")
            print(f"{Player.defense_use_left} use left for {item.name}")