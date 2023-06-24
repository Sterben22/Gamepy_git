import pygame
from pygame.locals import *

from gameManager.map import Map
from gameManager.player import Player
from gameManager.enemy import Enemy
from gameManager.collision import checkCollision
from gameManager.menu import *
from gameManager.config import *

class Game():
    def __init__(self, config: Config):
        self._running = True
        self.gaming = Gaming.GAME
        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode((config.MAP.WIDTH, config.MAP.HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.config = config

        self.mapa = Map(config.MAP)
        self.player = Player(config.PLAYER)
        self.enemy = list(map(lambda _: Enemy(config.ENEMY), [None]*config.ENEMY_NUMBER))

        self.score = 0

    def on_init(self):
        pygame.init()
        self.clock.tick(60)

    def on_restart(self):
        self.player = Player(self.config.PLAYER)
        self.enemy = list(map(lambda _: Enemy(self.config.ENEMY), [None]*self.config.ENEMY_NUMBER))
    
    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        pass

    def on_loop(self):
        for enemy in self.enemy:
            enemy.move(self.player)
            if checkCollision(self.player,enemy):
                self.gaming = Gaming.GAMEOVER

    def on_event(self, event):

        if (self.gaming == Gaming.GAME):
            keys = pygame.key.get_pressed()
            self.player.move(keys)

        match event.type:
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_q:
                        self.on_exit()
                    case pygame.K_p:
                        match self.gaming:
                            case Gaming.PAUSE:
                                self.gaming = Gaming.GAME
                            case Gaming.GAME:
                                self.gaming = Gaming.PAUSE
                            case Gaming.GAMEOVER:
                                pass
                    case pygame.K_r:
                        if (self.gaming == Gaming.GAMEOVER):
                            self.on_restart()
                            self.gaming = Gaming.GAME

            case pygame.QUIT:
                self.on_exit()

    def on_render(self):
        self.mapa.render(self._display_surf)
        self.player.render(self._display_surf)
        for enemy in self.enemy:
            enemy.render(self._display_surf)
        self._display_surf.blit(pygame.font.Font('freesansbold.ttf', 20).render("Points: " + str(self.score), True, (255,255,255)), (5 , 5))
        pygame.display.flip()

    def on_execute(self):
        self.on_init()
        while self._running:  

            for event in pygame.event.get():
                self.on_event(event)

            match self.gaming:
                case Gaming.GAME:
                    self.on_render()
                    self.on_loop()
                case Gaming.PAUSE:
                    pause(self._display_surf)
                case Gaming.GAMEOVER:
                    game_over(self._display_surf)
        pygame.quit()
