import RPi.GPIO as GPIO

import time



class front_sensor():

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.TRIG = 20
        self.ECHO = 21
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        self.distance = 99999
        self.cycle_on = False
        self.i = 1
        print " front sensor initialized "


    def read_distance(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO) == 0:
            self.pulse_start = time.time()

        while GPIO.input(self.ECHO) == 1:
            self.pulse_end = time.time()

        self.pulse_duration = self.pulse_end - self.pulse_start

        self.tmp_distance = self.pulse_duration * 17150
        if self.distance == 0 :
            self.distance = round(self.tmp_distance, 2)
        elif ( self.tmp_distance  < 3000):
          self.distance = round(self.tmp_distance, 2)

        #else:
        #   self.distance = 99999


    def read_distance_cycle(self):
        self.cycle_on = True
        while self.cycle_on == True:
          self.read_distance()
          time.sleep(.1)

        print " !!!!!!!!!!!!!!front distance : stop reading in cycle"

    def stop_reading(self):
        self.cycle_on = False
        print "******** stop reading"


class rear_sensor():

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.TRIG = 12
        self.ECHO = 16
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        self.distance = 99999
        self.cycle_on = False
        self.i = 1
        print " rear sensor initialized "


    def read_distance(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO) == 0:
            self.pulse_start = time.time()

        while GPIO.input(self.ECHO) == 1:
            self.pulse_end = time.time()

        self.pulse_duration = self.pulse_end - self.pulse_start

        self.tmp_distance = self.pulse_duration * 17150
        if self.distance == 0 :
            self.distance = round(self.tmp_distance, 2)
        elif ( self.tmp_distance  < 3000):
          self.distance = round(self.tmp_distance, 2)


    def read_distance_cycle(self):
        self.cycle_on = True
        while self.cycle_on == True:
          self.read_distance()
          time.sleep(.1)

        print " !!!!!!!!!!!!!!rear distance : stop reading in cycle"

    def stop_reading(self):
        self.cycle_on = False
        print "******** stop reading"

