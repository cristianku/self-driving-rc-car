import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
#gpio.setmode(gpio.BOARD)


# set the pin direction
gpio.setup ( 5, gpio.OUT)
gpio.setup ( 6, gpio.OUT)
gpio.setup ( 13, gpio.OUT)
gpio.setup ( 19, gpio.OUT)
gpio.setup ( 26, gpio.OUT)

gpio.cleanup()