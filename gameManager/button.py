import pygame

from .menu import *

class Button():
    def __init__(self, image, scale):
        sprite = pygame.image.load(image)
        self._sprite = pygame.transform.scale(sprite, (sprite.get_width() * scale, sprite.get_height() * scale))
        self._rect = self._sprite.get_rect()

    def press(self, pos):
        return self._rect.collidepoint(pos)
