import pygame
from pygame.locals import *

from .config import *

class Map():
    def __init__(self, config: MapConfig):
        self.size = config.WIDTH, config.HEIGHT
        self.skin = config.BACKGROUND

    def render(self, surface):
        surface.blit(pygame.image.load(self.skin), (0, 0))
