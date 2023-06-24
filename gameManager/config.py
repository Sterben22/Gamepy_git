from enum import Enum

class Gaming(Enum):
    GAME = 1
    PAUSE = 2
    GAMEOVER = 3

class MapConfig():
    def __init__(self, width, height, skin = "img/fondo.jpg"):
        self.WIDTH = width
        self.HEIGHT = height
        self.BACKGROUND = skin

class PlayerConfig():
    def __init__(self, x, y, skin = "img/player/11.png"):
        self.X = x
        self.Y = y
        self.SKIN = skin

class EnemyConfig():
    def __init__(self, skin = "img/enemy/0.png"):
        self.SKIN = skin

class Config():
    def __init__(self, mapConfig: MapConfig, playerConfig: PlayerConfig, enemyConfig: EnemyConfig, enemyNumber: int):
        self.MAP = mapConfig
        self.PLAYER = playerConfig
        self.ENEMY = enemyConfig
        self.ENEMY_NUMBER = enemyNumber
