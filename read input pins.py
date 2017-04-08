import RPi.GPIO as gpio
import time

#gpio.setmode(gpio.BCM)
gpio.setmode(gpio.BOARD)


# set the pin direction
gpio.setup ( 13, gpio.IN)


value = gpio.input(13)

