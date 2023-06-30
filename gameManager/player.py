import pygame
from pygame.locals import *

from .config import *

class Player():
    def __init__(self, config: PlayerConfig):
        self.pos = config.X, config.Y
        self.sprite_original = pygame.image.load(config.SKIN)
        self._sprite = self.sprite_original 

    def move(self, keys):
        x = self.pos[0]
        y = self.pos[1]

        if keys[K_w]:
            y -= 5
            self._sprite = pygame.transform.rotate(self.sprite_original, 0)
        elif keys[K_a]:
            x -= 5
            self._sprite = pygame.transform.rotate(self.sprite_original, 90)
            
        elif keys[K_s]:
            y += 5
            self._sprite = pygame.transform.rotate(self.sprite_original, 180)
           
        elif keys[K_d]:
            x += 5
            self._sprite = pygame.transform.rotate(self.sprite_original, 270)
            

        # Update position
        self.pos = x, y

    def render(self, surface):
        surface.blit(self._sprite, self.pos)

    
