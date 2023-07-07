import pygame

class Music:
    def __init__(self, filepath="music/Pista_GameBattle.wav"):
        pygame.mixer.init()
        self.filepath = filepath

    def load_music(self):
        pygame.mixer.music.load(self.filepath)

    def play_effect(self):
        sound = pygame.mixer.Sound(self.filepath)
        sound.play()
    def play_music_back(self, loop=-1,volume=0):
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()
