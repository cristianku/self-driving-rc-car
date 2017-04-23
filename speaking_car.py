import pygame
import time


class speaking_car():

    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
        # pygame.mixer.music.load("clacson.wav")


    def play_quaranta(self):
        pygame.mixer.music.load("./audio/quaranta.wav")
        pygame.mixer.music.set_volume(1)

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    def play_cinquanta(self):
        pygame.mixer.music.load("./audio/cinquanta.wav")
        pygame.mixer.music.set_volume(1)

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    def play_sessanta(self):
        pygame.mixer.music.load("./audio/sessanta.wav")
        pygame.mixer.music.set_volume(1)

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    def play_settanta(self):
        pygame.mixer.music.load("./audio/settanta.wav")
        pygame.mixer.music.set_volume(1)

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
