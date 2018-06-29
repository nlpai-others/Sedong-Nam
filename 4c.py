#!/usr/bin/python

import matplotlib.pyplot as plt
import sys

# trainings (x,y) pairs
trainings = [[1,2],[3,6],[7,14],[2,4],[4,8]]

trainings_X = [row[0] for row in trainings]
trainings_Y = [row[1] for row in trainings]

import random
import time

#가정 : y = ax + b

best_a   = -1
best_b   = -1
err_min  = 1000
count    = 0

while True:
   a = random.uniform(0,10)   # a 의 값
   b = random.uniform(0,10)   # b 의 값

   err = 0
   count =  count + 1

   #오차
   for i, t_x in enumerate(trainings_X):
      y = a * t_x + b #가정값
      t_y = trainings_Y[i] # 실제값
      err += abs(y-t_y) # 오차
#      if err > 2.9 and err < 3.1:
#      if err < 0.01:
#         print ("a=", a, "b=", b, "err=", err)
#         sys.exit(1)
   if err < err_min:
      err_min = err
      best_a = a
      best_b = b

   print ("count = ", count)
   print ("a=", a, "b=", b, "err=", err)
   print ("  ", "best_a= ", best_a, "best_b = ", best_b, "err_min =", err_min)
   time.sleep(0.01)    