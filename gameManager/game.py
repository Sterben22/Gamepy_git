import pygame
from pygame.locals import *

from gameManager.map import Map
from gameManager.player import Player
from gameManager.enemy import Enemy
from gameManager.bullet import Bullet
from gameManager.collision import checkCollision
from gameManager.menu import *
from gameManager.config import *

class Game():
    def __init__(self, config: Config):
        self._running = True
        self.gaming = Gaming.MENU
        self.clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode((config.MAP.WIDTH, config.MAP.HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.config = config
        self.button = []
        self.move_tick = 0

        self.mapa = Map(config.MAP)
        self.player = Player(config.PLAYER, config.BULLET)
        self.enemys = list(map(lambda _: Enemy(config.ENEMY, (60, 60)), [None]))

        self.score = 0

    def on_init(self):
        pygame.init()

    def on_restart(self):
        self.player = Player(self.config.PLAYER, self.config.BULLET)
        self.enemys = list(map(lambda _: Enemy(self.config.ENEMY, (60, 60)), [None]))
        self.score = 0
    
    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        pass

    def on_loop(self):
        if self.move_tick > 0:
            self.move_tick -= 1

        dt = self.clock.tick(self.config.FRAME_RATE) / 1000
        for enemy in self.enemys:
            enemy.move(dt)
            if checkCollision(self.player,enemy):
                self.gaming = Gaming.GAMEOVER
        
        for bullet in self.player.bullets:
            bullet.move(dt)

    def on_event(self, event):
        if (self.gaming == Gaming.GAME and self.move_tick == 0):
            self.move_tick = 2
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move(Mov.UP)
            elif keys[pygame.K_a]:
                self.player.move(Mov.LEFT)            
            elif keys[pygame.K_s]:
                self.player.move(Mov.DOWN)
            elif keys[pygame.K_d]:
                self.player.move(Mov.RIGHT)

        match event.type:
            case pygame.QUIT:
                self.on_exit()
                
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
                            case _:
                                pass

                    case pygame.K_r:
                        if self.gaming == Gaming.GAMEOVER:
                            self.on_restart()
                            self.gaming = Gaming.GAME

                    case pygame.K_SPACE:
                        self.bullet.posicion(self.player.pos,self.player.direccion)
            case pygame.MOUSEBUTTONDOWN:
                if self.button[0].press(pygame.mouse.get_pos()):
                    self.gaming = Gaming.GAME
                if self.button[1].press(pygame.mouse.get_pos()):
                    self.gaming = Gaming.QUIT

            case pygame.QUIT:
                self.on_exit()

            case _:
                pass

    def on_render(self):
        self.mapa.render(self._display_surf)
        self.player.render(self._display_surf)
        for enemy in self.enemys:
            enemy.render(self._display_surf)
        for bullet in self.player.bullets:
            bullet.render(self._display_surf)

        self._display_surf.blit(pygame.font.Font('freesansbold.ttf', 20).render("Points: " + str(self.score), True, (255,255,255)), (5 , 5))
        pygame.display.flip()

    def on_execute(self):
        self.on_init()
        while self._running:  
            for event in pygame.event.get():
                self.on_event(event)
            match self.gaming:
                case Gaming.MENU:
                    self.mapa.render(self._display_surf)                    
                    self.button = screen_menu(self._display_surf)
                case Gaming.GAME:
                    self.on_render()
                    self.on_loop()
                case Gaming.PAUSE:
                    pause(self._display_surf)
                case Gaming.GAMEOVER:
                    game_over(self._display_surf)
                case Gaming.QUIT:
                    self._running = False
        pygame.quit()



