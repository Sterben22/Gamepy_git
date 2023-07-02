from enum import Enum
import pygame

class Gaming(Enum):
    MENU = 1
    GAME = 2
    PAUSE = 3
    GAMEOVER = 4
    QUIT = 5

class Ort(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Mov(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class MapConfig():
    def __init__(self, width, height, skin = "img/fondo.jpg"):
        self.WIDTH = width
        self.HEIGHT = height
        self.BACKGROUND = skin

class PlayerConfig():
    def __init__(self, x, y, speed, skin ="img/player/up.png"):
        self.X = x
        self.Y = y
        self.SPEED = speed
        self.SKIN = skin

class BulletConfig():
    def __init__(self, skin = "img/bullet/0.jpg"):
        self.SKIN = skin

class EnemyConfig():
    def __init__(self, speed, skin = "img/enemy/0.png"):
        self.SKIN = skin
        self.SPEED = speed

class Config():
    def __init__(self, mapConfig: MapConfig, playerConfig: PlayerConfig, enemyConfig: EnemyConfig, bulletConfig: BulletConfig, frames: int):
        self.MAP = mapConfig
        self.PLAYER = playerConfig
        self.ENEMY = enemyConfig
        self.BULLET = bulletConfig
        self.FRAME_RATE = frames

