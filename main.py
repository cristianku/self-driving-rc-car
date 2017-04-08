import leds
import ultrasonic_sensors
import system_info
import engines
import servo


import time
import threading

import RPi.GPIO as GPIO


# def stop_everything():
#     engine.desired_direction = "stay"
#     time.sleep(.5)
#     # turn off the engine
#     engine.engine_running = False
#     servo.servo_turned_on = False
#     # turn off
#     # right_led.turn_off()
#     # left_led.turn_off()
#     front_distance.stop_reading()
#     rear_distance.stop_reading()
#     print " ------------------ "
#     print " cleaning up ..."
#     GPIO.cleanup()
#     exit()

#left_led = leds.left_led()
#t_left_led = threading.Thread(target=left_led.turn_on)
#t_left_led.start()

#right_led = leds.right_led()
#t_right_led = threading.Thread(target=right_led.turn_on)
#t_right_led.start()

# start read front distance Thread
front_distance = ultrasonic_sensors.front_sensor()
t_front_distance = threading.Thread(target=front_distance.read_distance_cycle)
t_front_distance.start()

# start read front distance Thread
rear_distance = ultrasonic_sensors.rear_sensor()
t_rear_distance = threading.Thread(target=rear_distance.read_distance_cycle)
t_rear_distance.start()

#time.sleep(5)
# engine = engines.engine()
# t_engine = threading.Thread(target=engine.start_engine )
# t_engine.start()


servo = servo.servo()
t_servo = threading.Thread(target=servo.start_servo )
t_servo.start()

time.sleep(1)

# engine.desired_speed = 80
# engine.acceleration = 2
# if   front_distance.distance < 40 and rear_distance.distance > 40:
#     engine.desired_direction ="backward"
# elif front_distance.distance > 40 :
#     engine.desired_direction ="forward"
# else:
#     print  " STOP EVERYTHING NO ENOUGH SPACE TO MOVE"
#     stop_everything()
# engine.desired_direction ="forward"

turns_to_left = 0
start_time = time.time()
end_cycle = False
last_turn_to_left = time.time()
time_in_turn_left = 0
last_turn_to_left = 0
obstacle_avoided = False

while True:
    print " front distance " , front_distance.distance
    print " rear distance ", rear_distance.distance
    time.sleep(0.3)
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

print " DOPO CICLO !!!"
print " DOPO CICLO !!!"
print " DOPO CICLO !!!"
print " DOPO CICLO !!!"
print " DOPO CICLO !!!"
time.sleep(0.01)

stop_everything()