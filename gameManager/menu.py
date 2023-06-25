import pygame
from pygame.locals import *

def game_over(screen):
    game_over_text = pygame.font.Font('freesansbold.ttf', 64).render("GAME OVER", True, (255,255,255))
    restart_text = pygame.font.Font('freesansbold.ttf', 64).render("PRESS R", True, (255,255,255))
    to_text = pygame.font.Font('freesansbold.ttf', 64).render("TO RESTART", True, (255,255,255))
    screen.blit(game_over_text, (190, 200))
    screen.blit(restart_text, (260, 280))
    screen.blit(to_text, (200, 360))

    pygame.display.flip()    

def pause(screen):
    game_over_text = pygame.font.Font('freesansbold.ttf', 64).render("PAUSE", True, (255,255,255))
    screen.blit(game_over_text, (280, 260))
    pygame.display.flip()
    
    
