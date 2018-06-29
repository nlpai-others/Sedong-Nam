#!/usr/bin/python

import matplotlib.pyplot as plt

# trainings (x,y) pairs
training = [[1,2],[3,6],[7,14],[2,4],[4,8]]

training_X = [row[0] for row in trainings]
training_Y = [row[1] for row in trainings]

import random
import time

# ���� : y = ax + b

while True:
   a = random.uniform(0,10)
   b = random.uniform(0,10)

   err = 0

   #����
   for i, t_x in enumerate(trainings_X):
       y = a * t_x + b #������
       t_y = trainings_Y[i] # ������
       err += abs(y-t_y) # ����
   print ("a=", a, "b=", b, "err=", err)
   time.sleep(1)