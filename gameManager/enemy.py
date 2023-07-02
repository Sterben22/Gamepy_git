import pygame
from .config import *

class Enemy():
    def __init__(self, config: EnemyConfig, position):
        self.pos = position
        self._sprite = pygame.image.load(config.SKIN)
        self.speed = config.SPEED
             
    def move(self, dt):
        x = self.pos[0]
        y = self.pos[1]

        y += self.speed*dt
        
        # Update position
        self.pos = x, y
            
    def render(self, surface):
        surface.blit(self._sprite, self.pos)
