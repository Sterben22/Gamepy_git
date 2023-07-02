import pygame
from pygame.locals import *

from .config import *
from .bullet import *

class Player():

    def __init__(self, playerConfig: PlayerConfig, bulletConfig: BulletConfig):
        self.pos = playerConfig.X, playerConfig.Y
        self._sprite = pygame.image.load(playerConfig.SKIN)
        self.ort = Ort.UP
        self.speed = playerConfig.SPEED 
        self.bulletConfig = bulletConfig
        self.bullets = []

    def shoot(self):
        self.bullets.append(Bullet(self.bulletConfig, self.pos, self.ort))
        
    def move(self, mov):
        x = self.pos[0]
        y = self.pos[1]

        match mov:
            case Mov.UP:
                y -= self.speed
                self.ort = Ort.UP

            case Mov.DOWN:
                y += self.speed
                self.ort = Ort.DOWN

            case Mov.LEFT:
                x -= self.speed
                self.ort = Ort.LEFT

            case Mov.RIGHT:
                x += self.speed
                self.ort = Ort.RIGHT

        # Update position
        self.pos = x, y

    def getRotatedSprite(self):
        match self.ort:
            case Ort.UP:
                return pygame.transform.rotate(self._sprite, 0)
            case Ort.DOWN:
                return pygame.transform.rotate(self._sprite, 180)
            case Ort.LEFT:
                return pygame.transform.rotate(self._sprite, 90)
            case Ort.RIGHT:
                return pygame.transform.rotate(self._sprite, 270)

    def render(self, surface):
        surface.blit(self.getRotatedSprite(), self.pos)

