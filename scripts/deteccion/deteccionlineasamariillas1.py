# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:06:21 2015

@author: jorge
"""

import cv2

from bordes import bord 
portcamera=0
cap = cv2.VideoCapture(portcamera)
cap.set(6,10)

while(1):

    # Take each frame
    _, img = cap.read()
    bord(img)  
              
    cv2.imshow('edges',img)
    k = cv2.waitKey(5) & 0xFF    
    if k == 27:
        break

cv2.destroyAllWindows()