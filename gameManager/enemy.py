
import pygame
from pygame.locals import *

class Enemy():
    def __init__(self, x, y, path) -> None:
        self.pos = self.x,self.y = x,y
        self.change = self.change_x,self.change_y = 1.2 , 1.5
        self._sprite = pygame.image.load(path).convert()
        self.w = self._sprite.get_width()
        self.h = self._sprite.get_height()
        self.life = True
    

    def move(self, player):
        if self.y >= 450:
            if abs(player.x - self.x) < 80:
                self.y = 2000
                
                pass
        
        if self.x <= 735 or self.x>=0:
            self.x += self.change_x
            self.change_x *= -1
            self.y += self.change_y
            
            self.pos = self.x,self.y



if __name__ == "__main__" :
    theApp = Enemy()