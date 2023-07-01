import pygame
from pygame.locals import *
from .config import *
class Bullet():
    def __init__(self,config:BulletConfig) -> None:
        # True - la bala se mueve
        # False - la bala no se mueve
        self.sprite_original = pygame.image.load(config.SKIN)
        self._sprite = self.sprite_original
        self.pos = (-10,-10)
        self.change = 0,0
        self.state = False

    
    def posicion(self,player_pos,player_direccion):
        self.state = True
        x = player_pos[0]
        y = player_pos[1]

        match player_direccion:
            case 0:
                self._sprite = pygame.transform.rotate(self.sprite_original, 0)
                self.change = 0,-1
            case 1:
                self._sprite = pygame.transform.rotate(self.sprite_original, 270)
                self.change = 1,0
            case 2:
                self._sprite = pygame.transform.rotate(self.sprite_original, 180)
                self.change = 0,1
            case 3:
                self._sprite = pygame.transform.rotate(self.sprite_original, 90)
                self.change = -1,0

        self.pos = x, y


    def move(self):
        x = self.pos[0]
        y = self.pos[1]
        
        if self.pos[0] <= 735 or self.pos[1] >= 0:
            # Update change
            x += self.change[0]
            y += self.change[1]
            
            # Update position
            self.pos = x, y
    
    def render(self, surface):
        surface.blit(self._sprite, self.pos)