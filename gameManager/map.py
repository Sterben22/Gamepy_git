import pygame
from pygame.locals import *

from .config import *

class Map():
    def __init__(self, config: MapConfig):
        self.size = config.WIDTH, config.HEIGHT
        self.skin = pygame.transform.scale(pygame.image.load(config.BACKGROUND), self.size)

    def render(self, surface):
        surface.blit(self.skin, (0, 0))
