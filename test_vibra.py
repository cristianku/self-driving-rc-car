#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math as m 

class Sw40(object):
    """docstring for Senal"""
    def __init__(self, pin ):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.callback, bouncetime=1)
        self.count = 0 

    def callback(self , pin):
        self.count += 1



def main():
    sensor = Sw40(27)
    try:
        while True:

            time.sleep(.01)
            if sensor.count >=5:
                print "vibration detected "
                sensor.count = 0



    except KeyboardInterrupt:
        GPIO.cleanup()



if __name__ == '__main__':
    main()