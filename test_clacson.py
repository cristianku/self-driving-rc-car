import leds
import ultrasonic_sensors
import system_info
import engines
import servo
import clacson
import accelerometr
import smbus

import time
import threading
import speaking_car
import pygame

import RPi.GPIO as GPIO



clacson = clacson.clacson()
t_clacson = threading.Thread(target=clacson.main )
t_clacson.start()
#     #
clacson.clacson_on = True
clacson.play_short = True
time.sleep(5)
#     acc.velocity = 0

speaking_car = speaking_car.speaking_car()

speaking_car.play_cinquanta()
time.sleep(0.5)

#acc.stop()

# clacson = clacson.clacson()
# t_clacson = threading.Thread(target=clacson.main )
# t_clacson.start()
#
# clacson.clacson_on = True


# while True:
#     print " front distance " , front_distance.distance
#     print " rear distance ", rear_distance.distance
#     time.sleep(0.3)
#  while end_cycle == False:
#     time.sleep(0.1)
#     if time.time() - start_time > 10 :
#         end_cycle = True

    # if rear_distance.distance < 40 and front_distance.distance < 40 :
    #       print " NON MI MUOVO !!!!!!!"
    #       print " NON MI MUOVO !!!!!!!"
    #       print " NON MI MUOVO !!!!!!!"
    #       print " NON MI MUOVO !!!!!!!"
    #       print " NON MI MUOVO !!!!!!!"
    #       print " NON MI MUOVO !!!!!!!"
    #       servo.turning_time = 0
    #       servo.desired_degree = 0
    #       end_cycle = True
#
    # if engine.actual_direction== "forward":
    #     if  front_distance.distance >= 100 :
    #         print " front distance ", front_distance.distance
    #         if last_turn_to_left > 0:
    #             servo.desired_degree = 0
    #             obstacle_avoided = True
    #             engine.acceleration = 2
    #             engine.desired_speed = 50
    #             time.sleep(.5)
    #             print "returning straight  "
    #             print "returning straight  "
    #             print "returning straight  "
    #             print "returning straight  "
    #             servo.turning_time = 0
    #             servo.desired_degree = 0
    #             servo.desired_degree = +35
    #             engine.desired_speed = 50
    #             engine.acceleration = 2
    #
    #             time.sleep(1)
    #             servo.desired_degree = 0
    #             time.sleep(1)
    #             end_cycle = True
    #
    #
    #     if obstacle_avoided == False:
    #         if  40 < front_distance.distance < 100:
    #             print " front distance ", front_distance.distance
    #             if servo.actual_degree == 0 :
    #                 servo.turning_time = 0.3
    #                 servo.desired_degree = -35
    #                 last_turn_to_left = time.time()
    #                 print "TRYING TO AVOID OBSTACLE TURNING LEFT = "
    #
    #     if front_distance.distance <= 40 and obstacle_avoided == False:
    #         print " ostacolo DAVANTI TROPPO VICINO !!!! INTERROMPO !!!!"
    #         # servo.turning_time = 0
    #         # servo.desired_degree = +25
    #         #
    #         # engine.desired_direction = "backward"
    #         # engine.desired_speed = 70
    #         # engine.acceleration = 3
    #         # time.sleep(1.5)
    #         # servo.desired_degree = 0
    #         # engine.desired_direction = "forward"
    #         engine.desired_direction = "stay"
    #         end_cycle = True
    #
    #         # if engine.actual_direction== "backward":
    # #     if rear_distance.distance < 40:
    # #         print " ostacolo dietro !!!!"
    # #         print " ostacolo dietro !!!!"
    # #         print " ostacolo dietro !!!!"
    # #         print " ostacolo dietro !!!!"
    # #         servo.turning_time = 0
    # #         servo.desired_degree = 15
    # #         engine.desired_speed = 70
    # #         engine.acceleration = 2
    # #         engine.desired_direction = "forward"

# time.sleep(0.01)
clacson.clacson_on = False

time.sleep(.5)
    #stop_everything()