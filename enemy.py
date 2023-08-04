import random
from game_entity import GameEntity
from player import Player

class Enemy(GameEntity):
    player_defense_use_left = 3

    def __init__(self, name, x, y, damage, health):
        super().__init__(name, x, y)
        self.health = health
        self.damage = damage
    
    def move(self, dx, dy):
        super().move(dx, dy)

    def attack(self, player):
        if self.health > 0:
            attack_value = random.randint(self.damage - 10, self.damage)
            if Enemy.player_defense_use_left > 0 and player.defense_boost > 0:
                attack_value -= player.defense_boost
                attack_value = max(attack_value, 0)
                player.health -= attack_value
                print(f"{self.name} dealt {attack_value} damage on {player.name}. \n{player.name}'s health is: {player.health}")
                Enemy.player_defense_use_left -= 1
                print(f"{Enemy.player_defense_use_left} uses left for player's defense.")
            else:
                player.health -= attack_value
                print(f"{self.name} dealt {attack_value} damage on {player.name}. \n{player.name}'s health is: {player.health}")