# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:16:43 2018

M/D/1 queue model - exponential arrivals, constanct service time, one queue
"""
import numpy as np
import time
start = time.time()

lamb = 10.                                              #  car arrival rate per minute
service = 7                                             #  car exit rate off island per minute
maxArrival = 100                                        #  maximum number of cars tp ,pve through the queue

numInQue = 0
arrive = 0
for i in range(20):                                     #  number of time steps in minutes
    if arrive < maxArrival:                             #  check to see if we have all the cars
        x = int(np.random.exponential(lamb))            #  can have zero arrivals; need to add +1 for > zero arrivals
    else:
        x = 0                                           #  we have all the cars
        arrive = maxArrival                             #  cap at maximum number of cars
    arrive = arrive + x                                 #  keep track of the total arrivals so the previous check works
    numInQue = numInQue + (x - service)                 #  how many cars in the queue
    if numInQue < 1:  numInQue = 0                      #  cannot have negative cars in the queue
    if arrive >= maxArrival and numInQue == 0: break    #  all cars and arrived and all cars have been serviced
    print(i+1, x, service, numInQue, arrive)              # keep track of where we are

print('')
print(time.time()-start)
