import pygame

pygame.mixer.init(frequency=44400, size=-16, channels=2, buffer=4096)
#pygame.mixer.music.load("clacson.wav")
pygame.mixer.music.load("clacson_short.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    continue

