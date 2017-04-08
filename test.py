import RPi.GPIO as gpio
import time

import engines
import threading


gpio.setmode(gpio.BCM)
#gpio.setmode(gpio.BOARD)


# set the pin direction
gpio.setup ( 23, gpio.OUT)
gpio.setup ( 18, gpio.OUT)



gpio.output ( 18, True)
gpio.output ( 23, True)

time.sleep(1)
gpio.output ( 18, False)
gpio.output ( 23, False)



engine = engines.engine()
t_engine = threading.Thread(target=engine.start_engine )
t_engine.start()

engine.desired_direction = "backward"
engine.desired_speed = 70
engine.acceleration = 3
time.sleep(0.2)
engine.desired_direction = "stay"


gpio.cleanup()



