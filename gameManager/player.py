import pygame
from pygame.locals import *

from .config import *

class Player():
    def __init__(self, config: PlayerConfig):
        self.pos = config.X, config.Y
        self._sprite = pygame.image.load(config.SKIN).convert()

    def move(self, keys):
        x = self.pos[0]
        y = self.pos[1]

        if keys[K_w]:
            y -= 5
        elif keys[K_a]:
            x -= 5
        elif keys[K_s]:
            y += 5
        elif keys[K_d]:
            x += 5

        # Update position
        self.pos = x, y

    def render(self, surface):
        surface.blit(self._sprite, self.pos)
