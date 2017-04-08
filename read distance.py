import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

trig = 26
echo = 19

def trig_measurement():
    gpio.output(trig,1)
    time.sleep(0.00001)
    gpio.output(trig,0)

def calc_distance():
    while gpio.input(echo )  == 0:
        pass
    start = time.time()

    while gpio.input(echo) == 1 :
        pass
    stop = time.time()
    gpio.cleanup()

    return ( stop - start ) * 170


#gpio.setmode(gpio.BOARD)


gpio.cleanup()
gpio.setmode(gpio.BCM)
gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

trig_measurement()

print calc_distance()




