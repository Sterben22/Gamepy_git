import pygame
from pygame.locals import *

def checkCollision(player, enemy):
    rect1 = pygame.Rect(player.pos[0], player.pos[1], player._sprite.get_width(), player._sprite.get_height())
    rect2 = pygame.Rect(enemy.pos[0] , enemy.pos[1] , enemy._sprite.get_width() , enemy._sprite.get_height())
    return rect1.colliderect(rect2)
