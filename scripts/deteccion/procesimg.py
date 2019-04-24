# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:02:43 2015

@author: jorge
"""
import cv2
import numpy as np
def proc_img(img):
    
            
    #img = cv2.imread(imag)
    
    
    theta1a=np.pi/2
    theta2a=np.pi/2
    theta3a=np.pi/2
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower = np.array([17,50,50])
    upper = np.array([23,255,255])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(img,img, mask= mask)
    res = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    res=res.astype(np.uint8)
    edges = cv2.Canny(res,300,300,apertureSize=3)
    lines = cv2.HoughLines(edges,1,np.pi/360,150)

    
    return rho, theta