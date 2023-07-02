import pygame
from .button import Button

def centerRect(width, height, sprite, x, y):
    sprite_rect = sprite.get_rect()
    sprite_rect.center = (width / 2 + x, height / 2 - y)
    return sprite_rect

def screen_menu(surface):
    width = surface.get_width()
    height = surface.get_height()

    startGame = Button("img/start_btn.png", 0.8)
    exitGame = Button("img/exit_btn.png", 0.8)

    startGame._rect = centerRect(width, height, startGame._sprite, -180, 0)
    exitGame._rect = centerRect(width, height, exitGame._sprite, 180, 0) 

    surface.blit(startGame._sprite, startGame._rect)
    surface.blit(exitGame._sprite, exitGame._rect)

    pygame.display.flip()

    return startGame, exitGame

def game_over(surface):
    width = surface.get_width()
    height = surface.get_height()

    gameover = pygame.font.Font('freesansbold.ttf', 64).render("GAME OVER", True, (255,255,255))
    restart = pygame.font.Font('freesansbold.ttf', 64).render("PRESS R TO RESTART", True, (255,255,255))
    
    surface.blit(gameover, centerRect(width, height, gameover, 0, 32))
    surface.blit(restart, centerRect(width, height, restart, 0, -32))

    pygame.display.flip()    

def pause(surface):
    width = surface.get_width()
    height = surface.get_height()

    pause = pygame.font.Font('freesansbold.ttf', 64).render("PAUSE", True, (255,255,255))
    
    surface.blit(pause, centerRect(width, height, pause, 0, 0))

    pygame.display.flip()
    
    
