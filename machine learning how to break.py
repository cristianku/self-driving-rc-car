from sklearn import svm

import RPi.GPIO as gpio

import time
import random

import simplejson

learn_cases = []

output_test_cases = []



file = open('test_cases.json' ,'r')

learn_cases = simplejson.loads(file)

file.close()


file = open('output_test_cases.json' ,'r')

output_test_cases = simplejson.loads(file)

file.close()

# fit machine learning SVM

from sklearn import svm

clf = svm.SVC()

clf.fit( learn_cases, output_test_cases)



#gpio.setmode(gpio.BCM)
gpio.setmode(gpio.BOARD)

# ultrasonic distance
forw = 7
back = 11

left = 13
right = 15

# set the pin direction
gpio.setup ( forw, gpio.OUT)
gpio.setup ( back, gpio.OUT)
gpio.setup ( left, gpio.OUT)
gpio.setup ( right, gpio.OUT)

# ultrasonic distance
trig = 38
echo = 40

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)


def trig_measurement():
    gpio.output(trig,1)
    time.sleep(0.00001)
    gpio.output(trig,0)


def actual_distance():
    while gpio.input(echo )  == 0:
        pass
    start = time.time()

    while gpio.input(echo) == 1 :
        pass
    stop = time.time()
    gpio.cleanup()

    return ( stop - start ) * 170


def if_start_break(start_time):

    final_object_distance = clf.predict([time.time() - start_time, actual_distance()])

    if (final_object_distance() <= 10 ):
        return actual_distance
    else:
        return 0
    end

def go_forward():
    gpio.output(forw, True)
    gpio.output(back, False)

def go_back():
    gpio.output(forw ,False)
    gpio.output(back, True)

def engine_off():
    gpio.output(forw, False)
    gpio.output(back, False)


def return_to_distance(distance):
    go_back()
    stop = 0
    while stop == 0:
       if actual_distance() <= distance:
           stop = 1
    engine_off()


def learn():

    start_time =time.time()

    go_forward()

    stop = 0
    while stop == 0:

        # stops execution after 6 seconds
        if time.time() > start_time  + 6 :
            distance_start_break = actual_distance()
            speed_at_start_break = time.time() - start_time
            stop = 1

        if (if_start_break(start_time)):
            distance_start_break = actual_distance()
            speed_at_start_break = time.time() - start_time
            stop = 1

    #read distance after break:

    gpio.output(7, 0)
    gpio.output(11, 0)

     # todo please wait until the vehicle really stops
     # now for simplicity waiting 1 seconds after turning off engine
    time.sleep(1)

    distance_after_break = actual_distance()

    print ' *********  starting break  ********* '
    print '  distance start break               ' + distance_start_break
    print '  speed ( time delta from moving )   ' + speed_at_start_break
    learn_cases.append[distance_start_break,speed_at_start_break ]

    output_test_cases.append(distance_after_break)

    print 'distance stop break  ' + distance_after_break

    # refit

    clf.fit(learn_cases, output_test_cases)

    return_to_distance(100)


learn()

learn()

learn()

learn()

# save testcases to a file

f= open('test_cases.json' ,'w')

simplejson.dump(learn_cases, f)

f.close()

# save output test cases to a file

f= open('output_test_cases.json' ,'w')

simplejson.dump(output_test_cases, f)

f.close()






