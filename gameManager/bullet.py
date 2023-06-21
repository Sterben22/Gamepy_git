import pygame
from pygame.locals import *

class Bullet():
    def __init__(self) -> None:
        # Bala
        # rest - la bala se mueve
        # fire - la bala no se mueve
        self._sprite = pygame.image.load('img/bullet.png')
        self.pos = (0,500)
        self.change = (0,3)
        self._state = "rest"
    
    def bullet(self):
        self._state = "fire"
    




if __name__ == "__main__" :
    theApp = Bullet()