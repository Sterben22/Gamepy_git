import pygame
from pygame.locals import *

class Enemy():
    def __init__(self, pos, change, path) -> None:
        self.pos = pos
        self.change = change
        self._sprite = pygame.image.load(path).convert()
        self.w = self._sprite.get_width()
        self.h = self._sprite.get_height()
    




if __name__ == "__main__" :
    theApp = Enemy()