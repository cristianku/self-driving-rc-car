import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup( 18, GPIO.OUT)
GPIO.output(18, True)

my_pwm = GPIO.PWM(18, 100)  # PIN / FREQUENCY
my_pwm.start(0)  # duty_cycle  = 50% up and 50% down
for i in range(100):
    time.sleep(0.05)
    my_pwm.ChangeDutyCycle(i)

my_pwm.stop()

GPIO.cleanup()