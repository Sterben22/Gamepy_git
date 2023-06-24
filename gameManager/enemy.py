import random

import pygame
from pygame.locals import *

from .collision import *
from .config import *
from .menu import *

class Enemy():
    def __init__(self, config: EnemyConfig):
        self.pos = random.randint(64, 737), random.randint(30, 180)
        self.change = 2, 2
        self._sprite = pygame.image.load(config.SKIN).convert()
    
    def move(self, player):
        x = self.pos[0]
        y = self.pos[1]

        if self.pos[1] >= 600:
            x = random.randint(64, 737)
            y = 0
        
        if self.pos[0] <= 735 or self.pos[1] >= 0:
            xc = self.change[0]
            xc *= -1
            # Update change
            self.change = xc, self.change[1]

            x += self.change[0]
            y += self.change[1]
            
            # Update position
            self.pos = x, y

    def render(self, surface):
        surface.blit(self._sprite, self.pos)
