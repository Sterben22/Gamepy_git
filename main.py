import random
import pygame
from pygame.locals import *

from gameManager.player import Player
from gameManager.enemy import Enemy
from gameManager.bullet import Bullet
from gameManager.collision import Collision


class Screen():
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.player = None
        self.enemy = None
        self.bullet = Bullet()
        self.clock = None
        self.collision = Collision()
        self.size = self.weight, self.height = 800, 600
        self.score = 0
        self.num_enemy = 8
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.blit(pygame.image.load("img/fondo.jpg"),(0,0))
        self._running = True
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.player = Player(20,20, "img/player/11.png")
        self.create_enemy()
 
    def on_event(self, event):
        if event.type == QUIT:
            self.on_exit()
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        
    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(pygame.image.load("img/fondo.jpg"),(0,0))
        self._display_surf.blit(self.player._sprite, self.player.pos)
        self._display_surf.blit(pygame.font.Font('freesansbold.ttf', 20).render("Points: " + str(self.score), True, (255,255,255)), (5 , 5 ))
        self.show_enemy()

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_exit(self):
        self._running = False

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
    
    def create_enemy(self):
        self.enemy = []
        for _ in range(self.num_enemy):
            sprite = 'img/enemy/0.png'
            pos = (random.randint(64, 737),random.randint(30, 180))
            change = (1.2,50)
            self.enemy.append(Enemy(pos,change,sprite))

    def show_enemy(self):
        #Funcion que se deberia llamar --> "on_render"
        for i in range(self.num_enemy):
            enemy = self.enemy[i]
            self._display_surf.blit(enemy._sprite, enemy.pos)

    def colission():
        pass
    def game_over():
        game_over_text = pygame.font.Font('freesansbold.ttf', 64).render("GAME OVER", True, (255,255,255))
        return game_over_text
 
if __name__ == "__main__" :
    theApp = Screen()
    theApp.on_execute()
