#!/usr/bin/python

import matplotlib.pyplot as plt

# trainings (x,y) pairs
training = [[1,2],[3,6],[7,14],[2,4],[4,8]]

training_X = [row[0] for row in trainings]
training_Y = [row[1] for row in trainings]

import random
import time

# 가정 : y = ax + b

while True:
   a = random.uniform(0,10)
   b = random.uniform(0,10)

   err = 0

   #오차
   for i, t_x in enumerate(trainings_X):
       y = a * t_x + b #가정값
       t_y = trainings_Y[i] # 실제값
       err += abs(y-t_y) # 오차
   print ("a=", a, "b=", b, "err=", err)
   time.sleep(1)