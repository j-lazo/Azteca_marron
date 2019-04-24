# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:53:33 2015

@author: jorge
"""

import cv2
import numpy as np
portcamera=2
cap = cv2.VideoCapture(portcamera)
#cap.set(3,1280)
#cap.set(4,1024)
cap.set(6,1000)


while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    #lower_blue = np.array([10,100,100])
    #upper_blue = np.array([30,255,255])

    # Threshold the HSV image to get only blue colors
    #mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()