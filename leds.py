import RPi.GPIO as GPIO
import time



class right_led(object):
    def __init__(self):
      GPIO.setmode(GPIO.BCM)
      self.LED_GPIO = 18
      GPIO.setup(self.LED_GPIO, GPIO.OUT)

    def turn_on(self):
        self.turned_on = True
        my_pwm = GPIO.PWM(self.LED_GPIO, 100)  # PIN / FREQUENCY
        my_pwm.start(0)  # duty_cycle  = 50% up and 50% down
        for i in range(100):
            time.sleep(0.05)
            my_pwm.ChangeDutyCycle(i)
        my_pwm.ChangeDutyCycle(0)
        time.sleep (0.3)
        my_pwm.ChangeDutyCycle(100)


        while self.turned_on == True:
            time.sleep(0.5)
        print "right led off "

    def turn_off(self):
        self.turned_on = False





class left_led(object):
    def __init__(self):
      GPIO.setmode(GPIO.BCM)
      self.LED_GPIO = 23
      GPIO.setup(self.LED_GPIO, GPIO.OUT)

    def turn_on(self):
        self.turned_on = True
        my_pwm = GPIO.PWM(self.LED_GPIO, 100)  # PIN / FREQUENCY
        my_pwm.start(0)  # duty_cycle  = 50% up and 50% down
        for i in range(100):
            time.sleep(0.05)
            my_pwm.ChangeDutyCycle(i)
        my_pwm.ChangeDutyCycle(0)
        time.sleep (0.3)
        my_pwm.ChangeDutyCycle(100)


        while self.turned_on == True:
            time.sleep(0.5)
        print "right led off "

    def turn_off(self):
        self.turned_on = False
