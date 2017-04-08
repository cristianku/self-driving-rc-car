import RPi.GPIO as GPIO
import time


class servo():
    def __init__(self):
      GPIO.setmode(GPIO.BCM)
      self.SERVO_LEFT  = 26
      self.SERVO_RIGHT = 19
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.SERVO_LEFT, GPIO.OUT)
      GPIO.setup(self.SERVO_RIGHT, GPIO.OUT)
      self.actual_degree = 0
      self.desired_degree = 0
      self.servo_cycles = 0
      self.turning_time = 0.3
      self.time_of_start_turning = time.time()


    def start_servo(self):
        GPIO.output(self.SERVO_LEFT, False)
        GPIO.output(self.SERVO_RIGHT, False)
        self.PWM_SERVO_LEFT = GPIO.PWM(self.SERVO_LEFT, 100)  # 400 is the frequency
        self.PWM_SERVO_RIGHT = GPIO.PWM(self.SERVO_RIGHT, 100)  # 400 is the frequency
        self.PWM_SERVO_LEFT.start(0)  # argument is the duty cycle from 0 to 100
        self.PWM_SERVO_RIGHT.start(0)  # argument is the duty cycle from 0 to 100

        self.servo_turned_on = True
        while self.servo_turned_on == True:
#            print "servo active"
             if self.actual_degree != self.desired_degree:
                if self.desired_degree > 0:
                   self.turn_right()
                elif self.desired_degree == 0:
                   self.straighten()
                elif self.desired_degree < 0:
                   self.turn_left()


             if self.turning_time > 0:  # this functionality can be disabled
                if abs(self.actual_degree) > 0:
                 if time.time() > self.time_of_start_turning + self.turning_time:
                   # print " time passed --> straighten the wheels !!"
                   # print " time passed --> straighten the wheels !!"
                   # print " time passed --> straighten the wheels !!"
                   # print " time passed --> straighten the wheels !!"
                   # print " time passed --> straighten the wheels !!"
                   self.straighten()

             time.sleep(.01)

        self.PWM_SERVO_RIGHT.ChangeDutyCycle(0)
        self.PWM_SERVO_LEFT.ChangeDutyCycle(0)



    def turn_left(self):
      self.time_of_start_turning = time.time()
      self.actual_degree = self.desired_degree
      servo_cycles = 0
      # print " desired degree : ", self.desired_degree

      print "TURNING LEFT !!!!!!! degree : " , self.desired_degree, " servo cycles ", self.calculate_servo_cycles(self.desired_degree)
      self.PWM_SERVO_RIGHT.ChangeDutyCycle(0)
      self.PWM_SERVO_LEFT.ChangeDutyCycle(self.calculate_servo_cycles(self.desired_degree))

    def turn_right(self):
      self.time_of_start_turning = time.time()
      self.actual_degree = self.desired_degree

      print "TURNING RIGHT !!!!!!! degree : " , self.desired_degree, " servo cycles ", self.calculate_servo_cycles(self.desired_degree)

      self.PWM_SERVO_RIGHT.ChangeDutyCycle(self.calculate_servo_cycles(self.desired_degree))
      self.PWM_SERVO_LEFT.ChangeDutyCycle(0)

    def straighten(self):
      self.time_of_start_turning = time.time()
      if self.actual_degree > 0 :
          # for i in range( self.calculate_servo_cycles(self.actual_degree), 0 ):
          #     time.sleep(.01)
          #     self.PWM_SERVO_RIGHT.ChangeDutyCycle(i)
          #     self.PWM_SERVO_LEFT.ChangeDutyCycle(0)

          self.PWM_SERVO_RIGHT.ChangeDutyCycle(0)
          self.PWM_SERVO_LEFT.ChangeDutyCycle(0)

      elif self.actual_degree < 0 :
          # for i in range( self.calculate_servo_cycles(self.actual_degree), 0 , -1):
          #     time.sleep(.01)
          #     self.PWM_SERVO_RIGHT.ChangeDutyCycle(i)
          #     self.PWM_SERVO_LEFT.ChangeDutyCycle(0)

          self.PWM_SERVO_RIGHT.ChangeDutyCycle(0)
          self.PWM_SERVO_LEFT.ChangeDutyCycle(0)

      self.actual_degree = 0
      self.desired_degree = 0
      servo_cycles = 0

      # print "straighten !!"


    def calculate_servo_cycles(self, desired_degree):
        servo_cycles = 0
        desired_degree = abs( desired_degree)
        if 1 <= desired_degree <= 15:
            servo_cycles = 50
        elif 16 <= desired_degree <= 25:
            servo_cycles = 65
        elif 26 <= desired_degree <= 35:
            servo_cycles = 80
        elif 36 <= desired_degree <= 45:
            servo_cycles = 90

        return servo_cycles


