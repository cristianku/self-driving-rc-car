import threading

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG_FRONT = 20
ECHO_FRONT = 21

TRIG_BACK = 12
ECHO_BACK = 16

# setup pins for front distance measurement
GPIO.setup(TRIG_FRONT,GPIO.OUT)
GPIO.setup(ECHO_FRONT,GPIO.IN)
GPIO.setup(TRIG_BACK,GPIO.OUT)
GPIO.setup(ECHO_BACK,GPIO.IN)

front_distance = 0

back_distance = 0

def calc_front_distance():
  global front_distance
  i = 1
  while i == 1 :
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_FRONT, GPIO.OUT)
    GPIO.setup(ECHO_FRONT, GPIO.IN)

    GPIO.output(TRIG_FRONT, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_FRONT, False)

    while GPIO.input(ECHO_FRONT)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO_FRONT)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    temp_front_distance = pulse_duration * 17150

    if ( temp_front_distance > 3000 ):
        pass
    else:
      front_distance = round(temp_front_distance, 2)

    time.sleep(0.5)


def calc_back_distance():
  global  back_distance

  i = 1
  while i == 1 :
    GPIO.output(TRIG_BACK, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_BACK, False)

    while GPIO.input(ECHO_BACK)==0:
      pulse_start = time.time()
    while GPIO.input(ECHO_BACK)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    temp_back_distance = pulse_duration * 17150

    if ( temp_back_distance > 3000 ):
        pass
    else:
        back_distance = round(temp_back_distance, 2)

    time.sleep(0.05)


thread_front_distance = threading.Thread(target=calc_back_distance)

thread_front_distance.start()

i= 1
while i == 1:

    print "FRONT DISTANCE : " , front_distance

    time.sleep(0.01)



GPIO.cleanup()




