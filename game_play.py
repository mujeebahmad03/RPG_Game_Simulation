class Game:
    def __init__(self):
        self.players = []
        self.enemies = []
        self.items = []

    def add_player(self, player):
        self.players.append(player)
    
    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def add_item(self, item):
        self.items.append(item)
    
    def handle_collisions(self):
        for player in self.players:
            for enemy in self.enemies:
                if player.x == enemy.x and player.y == enemy.y:
                    player.attack(enemy)
                    enemy.attack(player)
        
        for player in self.players:
            for item in self.items:
                if player.x == item.x and player.y == item.y:
                    print(f"{player.name} has collected {item.name} worth {item.value}")
                    player.use_item(item)
                    self.items.remove(item)
                    break
    
    def update_game_state(self):
        self.handle_collisions()
