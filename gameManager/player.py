import pygame
from pygame.locals import *

from .config import *

class Player():
    def __init__(self, config: PlayerConfig):
        self.pos = config.X, config.Y
        self._sprite = pygame.image.load(config.SKIN)
        self.ort = Ort.UP
        
    def move(self, keys):
        x = self.pos[0]
        y = self.pos[1]

        if keys[K_w]:
            y -= 5
            self.ort = Ort.UP

        elif keys[K_a]:
            x -= 5
            self.ort = Ort.LEFT

        elif keys[K_s]:
            y += 5
            self.ort = Ort.DOWN
           
        elif keys[K_d]:
            x += 5
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

