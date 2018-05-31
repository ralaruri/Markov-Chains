# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:58:54 2018

simple Markov model with 8 sites and potential change of states
"""
import numpy as np
import time

start = time.time()

#  set up connection data and list data
siteList = ['hotel', 'site1', 'site2', 'site3', 'site4', 'site5', 'site6', 'site7']
hotel = [.15, .3, .15, .4, 0, 0, 0, 0]
site1 = [.15, .15, 0, 0, .25, .45, 0, 0]
site2 = [.15, .25, .2, 0, 0, 0, .4 ,0]
site3 = [.4, 0 ,0, .15, 0 , 0, 0, .45]
site4 = [.8, 0, 0, 0, .2, 0, 0, 0]
site5 = [0, 0, .85, 0, 0, .15, 0, 0]
site6 = [.8, 0, 0, 0, 0, 0, .2, 0]
site7 = [.75, 0, 0, 0, 0, 0, 0, .25]
siteProb = [hotel, site1, site2, site3, site4, site5, site6, site7]

tour = []
curLoc = hotel
tour.append(siteList[0])                            # save the starting site
for i in range(5):
    x = np.random.uniform(0,1)                      #  use uniform random numbers since sum of all probs from a site is one
    ssum = 0                                        #  bookkeeping
    saveJ = 0                                       #  bookkeeping
    flag = 0                                        #  bookkeeping
    for j in range(len(curLoc)):                    #  loop through until you reach the random number threshold
        ssum = ssum + curLoc[j]                     #  keep track of the cumulative total
        if x <= ssum:                               #  when we meet the threshold, save where we are and do it again
            saveJ = j                               #  save which site we went to
            print(x, j, saveJ, curLoc[j], curLoc)
            flag = 1                                # cluggy way to break out
        if flag == 1: break                         # cluggy way to break out
    tour.append(siteList[saveJ])                    #  save where we went to
    curLoc = siteProb[saveJ]                        #  load that site's probabilities
    if saveJ == 0: break                            #  back to the hotel?, then done
    
print('')
print(tour)
#print(time.time()-start)