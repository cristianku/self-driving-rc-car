import pygame
import time


class clacson():

    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
        # pygame.mixer.music.load("clacson.wav")
        pygame.mixer.music.load("clacson_short.wav")
        pygame.mixer.music.set_volume(1)
        self.clacson_on = True
        self.play_short = False

    def main(self):

        while self.clacson_on == True:
            if self.play_short == True:
                self.play_short_fun()
                self.play_short = False
        print " exiting clacson"
        pygame.mixer.stop()
        pygame.mixer.fadeout(1)
        pygame.mixer.quit()


    def play_short_fun(self):
        print " playing short "
        for i in range(1,3):
            print " beep  " , i

            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                 continue
        print " here "

            #time.sleep ( 0.1)