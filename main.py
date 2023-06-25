from gameManager.game import Game
from gameManager.config import *

if __name__ == "__main__" :
    # Game configuration
    mapa = MapConfig(900, 700)
    player = PlayerConfig(400, 300, "img/player/up.png")
    enemy = EnemyConfig("img/enemy/0.png")
    bullet = BulletConfig("img/bullet/0.png")

    config = Config(mapa, player, enemy, bullet, 15)

    # Execute game
    game = Game(config)
    game.on_execute()
