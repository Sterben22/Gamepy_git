from gameManager.game import Game
from gameManager.config import *

if __name__ == "__main__" :
    # Game configuration
    mapa = MapConfig(800, 600)
    player = PlayerConfig(400, 300, "img/player/up.png")
    enemy = EnemyConfig("img/enemy/0.png")

    config = Config(mapa, player, enemy, 8)

    # Execute game
    game = Game(config)
    game.on_execute()
