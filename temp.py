import time

import system_info


x = 1
while True:
    i = 1
    while i < 10000:
       # print " front distance read ", front_distance.distance
       # print " rear distance read ", front_distance.distance
        t = time.time()
        i = i + 1
    print " CPU temperature ", system_info.getCPUtemperature()


    print "CPU USE ", system_info.getCPUuse()