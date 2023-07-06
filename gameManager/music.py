import pygame

class MusicPlayer:
    def __init__(self, filepath="music\Pista_GameBattle.wav"):
        pygame.mixer.init()
        self.filepath = filepath

    def load_music(self):
        pygame.mixer.music.load(self.filepath)

    def play_music(self, loop=1,volume=.5):
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)

    def stop_music(self):
        pygame.mixer.music.stop()
