import RPi.GPIO as GPIO
import time


class engine():

    def __init__(self):
      GPIO.setmode(GPIO.BCM)
      self.ENGINE_FW = 22
      self.ENGINE_BW = 13
      self.actual_speed   = 0


      self.changing_speed = False
      self.accelerate_or_decelerate_running = False
      self.stop_changing_speed = False
      self.actual_direction = "forward"
      self.desired_direction = "forward"


      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.ENGINE_FW, GPIO.OUT)
      GPIO.setup(self.ENGINE_BW, GPIO.OUT)

      self.actual_direction = "stay"
      self.desired_direction = "stay"
      self.desired_speed = 0
      self.actual_speed = 0
      self.acceleration= 1



    def set_engine_direction(self, direction):
        self.desired_direction = direction

    def pulse_back(self):
        # print " ===== PULSE BACK"
        self.go_bw(100)
        time.sleep(.01)
        self.go_bw(0)

    def pulse_forward(self):
        # print " ===== PULSE FORWARD"
        self.go_fw(100)
        time.sleep(.01)
        self.go_fw(0)

    def brake(self):
        # print " **************** "
        print "******* BRAKING "

        self.change_speed(0)
        time.sleep(.01)
        if self.actual_direction == "forward":
            self.pulse_back()
            self.pulse_back()
            self.pulse_back()
            self.pulse_back()
            self.pulse_back()
            self.pulse_back()
            self.pulse_back()
            self.pulse_back()
            self.pulse_back()
            self.pulse_back()

        if self.actual_direction == "backward":
            self.pulse_forward()
            self.pulse_forward()
            self.pulse_forward()
            self.pulse_forward()
            self.pulse_forward()
            self.pulse_forward()

        self.actual_direction = "stay"

    def start_engine(self):
#      self.pwm_obj.start(self.actual_speed)  # argument is the duty cycle from 0 to 100
        GPIO.output(self.ENGINE_FW, False)
        GPIO.output(self.ENGINE_BW, False)
        self.PWM_FW = GPIO.PWM(self.ENGINE_FW, 150)  # 400 is the frequency
        self.PWM_BW = GPIO.PWM(self.ENGINE_BW, 150)  # 400 is the frequency
        self.PWM_FW.start(0)  # argument is the duty cycle from 0 to 100
        self.PWM_BW.start(0)  # argument is the duty cycle from 0 to 100

        self.engine_running = True

        print "==============================="
        print "=== starting engine ============================"
        print "==============================="
        while self.engine_running == True:
#            print " while true in engine class"
          self.set_direction()
          self.set_speed()
          time.sleep(0.01)

        self.stop_engine()

      # time.sleep(1)

    def stop_engine(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ENGINE_FW, GPIO.OUT)
        GPIO.setup(self.ENGINE_BW, GPIO.OUT)
        GPIO.output(self.ENGINE_FW, False)
        GPIO.output(self.ENGINE_BW, False)
        print "Engine off -- end of class method "

    def change_speed(self, speed):
        if self.actual_direction =="stay" and self.actual_speed >  0:
            # print " change speed STAY ", speed
            self.go_fw(0)
            self.desired_speed = 0

        if self.actual_direction =="forward":
            # print " change speed go forward", speed
            self.go_fw(speed)
        if self.actual_direction =="backward":
            # print " change speed go backward", speed
            self.go_bw(speed)


    def go_fw(self, speed):
      self.actual_speed = speed
      self.PWM_FW.ChangeDutyCycle(self.actual_speed)
      self.PWM_BW.ChangeDutyCycle(0)
#      print " change in speed : ", self.actual_speed, "  direction : ",  self.actual_direction


    def go_bw(self, speed):
      self.actual_speed = speed
      self.PWM_FW.ChangeDutyCycle(0)
      self.PWM_BW.ChangeDutyCycle(self.actual_speed)
 #     print " change in speed : ", self.actual_speed, "  direction : ",  self.actual_direction

    def set_direction(self):
        if self.actual_direction != self.desired_direction:
            print " actual direction ", self.actual_direction, " desired direction ", self.desired_direction
            if self.actual_direction != "stay" or self.desired_direction == "stay":
                print " desired direction = ", self.desired_direction
                self.brake()

                #            print " Actual speed = " , self.actual_speed , " Desired = ", self.desired_speed


            if self.desired_direction == "forward":
                self.actual_direction = "forward"
                # print " ----> GOING FORWARD"
                GPIO.setmode(GPIO.BCM)
                self.go_fw(0)

            if self.desired_direction == "backward":
                self.actual_direction = "backward"
                # print " ----> GOING BACKWARD"
                GPIO.setmode(GPIO.BCM)
                self.go_bw(0)


    def set_speed(self):
#R        print "set speed  actual = ", self.actual_speed , " desired speed ", self.desired_speed
        if self.actual_speed < self.desired_speed:
                if self.actual_speed < 30:
                    self.actual_speed = 30
                else:
                    self.actual_speed = self.actual_speed + 2

                if self.actual_speed > 100:
                    self.actual_speed = 100
                self.change_speed(self.actual_speed)

                self.change_speed(self.actual_speed)

        if self.actual_speed > self.desired_speed:
                self.actual_speed = self.actual_speed - 2
                if self.actual_speed < 30:
                    self.actual_speed = 30
                self.change_speed(self.actual_speed)


        if self.acceleration == 1:
            time.sleep(.3)

        if self.acceleration == 2:
            time.sleep(.1)

        if self.acceleration == 3:
            time.sleep(.01)





