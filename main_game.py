import random
from game_play import Game
from player import Player
from enemy import Enemy
from item import Item

ahmad = Player('Ahmad', 0, 0, health=100, damage=10)
wolf = Enemy('Wolf', 3, 3, health=60, damage=25)
lion = Enemy('Lion', 2,2, health=70, damage=30)
elixir = Item('Elixir', 5,6, value=20, item_type='health')
mana_portion = Item('Mana Portion', 7, 2, value=10, item_type='attack')
sword = Item('Sword', 5, 2, value=30, item_type='attack')
shield = Item('Shield', 4, 2, value=30, item_type='defense')

game = Game()

game.add_player(ahmad)
game.add_enemy(wolf)
game.add_enemy(lion)
game.add_item(elixir)
game.add_item(mana_portion)
game.add_item(sword)
game.add_item(shield)


while True:
    for player in game.players:
        direction = input(f"{player.name}, enter your movement direction (w/s/a/d): ").lower()
        if direction == 'w':
            player.move(0, 1)
        elif direction == 's':
            player.move(0, -1)
        elif direction == 'd':
            player.move(1, 0)
        elif direction == 'a':
            player.move(-1, 0)
        else:
            print('Invalid direction. Try again')
            continue

    for enemy in game.enemies:
        enemy.move(random.randint(-1, 1), random.randint(-1, 1))

    game.update_game_state()

    defeated_players = [player for player in game.players if player.health <= 0]
    defeated_enemies = [enemy for enemy in game.enemies if enemy.health <= 0]

    if defeated_players:
        print("Defeated players:")
        for player in defeated_players:
            print(f"{player.name}")
        print("You lose!!!")
        break

    if len(defeated_enemies) == len(game.enemies):
        print("All enemies have been defeated. You win!!!")
        break
