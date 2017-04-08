import RPi.GPIO as gpio
import time



gpio.setmode(gpio.BOARD)

pwm_obj = gpio.pwm(8,400) #400 is the frequency


pwm_obj.start(100) # argument is the duty cycle from 0 to 100