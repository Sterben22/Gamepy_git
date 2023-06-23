import pygame
from pygame.locals import *

def isCollision(player, enemy):
    rect1 = pygame.Rect(player.x, player.y, player.w, player.h)
    rect2 = pygame.Rect(enemy.x, enemy.y, enemy.w, enemy.h)
    if rect1.colliderect(rect2):
        return True
    else:
        return False