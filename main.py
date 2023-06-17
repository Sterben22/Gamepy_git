import pygame
from pygame.locals import *

from gameManager.player import Player

class Screen():
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.player = None
        self.enemy = None
        self.clock = None
        self.size = self.weight, self.height = 1000, 700
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.blit(pygame.image.load("img/fondo.jpg"),(0,0))
        self._running = True
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.player = Player(20,20, "img/player/11.png")
 
    def on_event(self, event):
        if event.type == QUIT:
            self.on_exit()
        keys = pygame.key.get_pressed()
        
    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(pygame.image.load("img/fondo.jpg"),(0,0))
        self._display_surf.blit(self.player._sprite, self.player.pos)
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
 
 
if __name__ == "__main__" :
    theApp = Screen()
    theApp.on_execute()
