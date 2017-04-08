import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

trig = 20
echo = 21
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 12
ECHO = 16


# setup pins for front distance measurement
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def front_distance():

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150

  distance = round(distance, 2)

  return distance

i = 1
while i == 1:
    print front_distance()
    time.sleep(0.2)


GPIO.cleanup()