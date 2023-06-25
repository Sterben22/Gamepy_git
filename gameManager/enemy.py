import random,math

import pygame
from pygame.locals import *

from .collision import *
from .config import *
from .menu import *

class Enemy():
    def __init__(self, config: EnemyConfig):
        self.pos = random.randint(64, 737), random.randint(30, 180)
        self.change = 2, 2
        self._sprite = pygame.image.load(config.SKIN)
        self.speed=2
    
    def new_pos(self):
            x = random.randint(30, 800)
            y = 0
            self.pos = x, y
            
    def move(self):
        x = self.pos[0]
        y = self.pos[1]

        if self.pos[1] >= 720:
            x = random.randint(30, 800)
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

    def move_player(self,player):
        dx = player.pos[0] - self.pos[0]
        dy = player.pos[1] - self.pos[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance != 0:
            dx_normalized = dx / distance
            dy_normalized = dy / distance
            x += dx_normalized * self.speed
            y += dy_normalized * self.speed
        # Update position
            self.pos = x, y
            
    def render(self, surface):
        surface.blit(self._sprite, self.pos)
