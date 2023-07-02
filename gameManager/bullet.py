import pygame
from .config import *

class Bullet():
    def __init__(self, config: BulletConfig, pos, ort):
        self._sprite = pygame.image.load(config.SKIN)
        self.pos = pos
        self.ort = ort
        self.speed = 300
 
    def move(self, dt):
        x = self.pos[0]
        y = self.pos[1]
        
        match self.ort:
            case Ort.UP:
                y -= self.speed*dt
            case Ort.DOWN:
                y += self.speed*dt
            case Ort.LEFT:
                x -= self.speed*dt
            case Ort.RIGHT:
                x += self.speed*dt
 
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
