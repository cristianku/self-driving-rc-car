import RPi.GPIO as gpio
import time



gpio.setmode(gpio.BCM)
gpio.setup(6, gpio.OUT)
gpio.setup(13, gpio.OUT)
pwm_obj = gpio.PWM(6,100) #400 is the frequency
gpio.output(6, True)
gpio.output(6, False)

pwm_obj.start(80) # argument is the duty cycle from 0 to 100

#pwm_obj.ChangeDutyCycle(50) # assign a new duty cycle

time.sleep(1)
gpio.output(6, False)

# the frequency is not accurate on Raspberry



