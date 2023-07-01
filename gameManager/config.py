from enum import Enum

class Gaming(Enum):
    MENU = 1
    GAME = 2
    PAUSE = 3
    GAMEOVER = 4
    QUIT = 5

class MapConfig():
    def __init__(self, width, height, skin = "img/fondo.jpg"):
        self.WIDTH = width
        self.HEIGHT = height
        self.BACKGROUND = skin

class PlayerConfig():
    def __init__(self, x, y, skin ="img/player/up.png"):
        self.X = x
        self.Y = y
        self.SKIN = skin
class BulletConfig():
    def __init__(self, skin = "img/bullet/0.jpg"):
        self.SKIN = skin
class EnemyConfig():
    def __init__(self, skin = "img/enemy/0.png"):
        self.SKIN = skin

class Config():
    def __init__(self, mapConfig: MapConfig, playerConfig: PlayerConfig, enemyConfig: EnemyConfig, bulletConfig: BulletConfig,enemyNumber: int):
        self.MAP = mapConfig
        self.PLAYER = playerConfig
        self.ENEMY = enemyConfig
        self.BULLET = bulletConfig
        self.ENEMY_NUMBER = enemyNumber
