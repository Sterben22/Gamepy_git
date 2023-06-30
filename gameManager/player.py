import pygame
from pygame.locals import *

from .config import *
from .bullet import Bullet

class Player():
    def __init__(self, config: PlayerConfig):
        self.pos = config.X, config.Y
        self.sprite_original = pygame.image.load(config.SKIN)
        self._sprite = self.sprite_original
        
        self.direccion = 0
        

    def move(self, keys):
        x = self.pos[0]
        y = self.pos[1]

        if keys[K_w]:
            y -= 5
            self._sprite = pygame.transform.rotate(self.sprite_original, 0)
            self.direccion = 0

        elif keys[K_a]:
            x -= 5
            self._sprite = pygame.transform.rotate(self.sprite_original, 90)
            self.direccion = 3

        elif keys[K_s]:
            y += 5
            self._sprite = pygame.transform.rotate(self.sprite_original, 180)
            self.direccion = 2
           
        elif keys[K_d]:
            x += 5
            self._sprite = pygame.transform.rotate(self.sprite_original, 270)
            self.direccion = 1

        # Update position
        self.pos = x, y

    def render(self, surface):
        surface.blit(self._sprite, self.pos)

    
