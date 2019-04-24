# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:48:35 2015

@author: jorge
"""
import math as ma

def control_liena(theta1,theta2,y1l,y2l,x1l,x2l,y2r,y1r,x2r,x1r):
    
    
    t1=theta1*180/np.pi
    t2=180-theta2*180/np.pi
    
    
    ml=(y1l-y2l)/((x1l-x2l)*1.)
    mr=(y2r-y1r)/((x2r-x1r)*1.)
    
    bl=y1l-ml*x1l
    br=y1r-mr*x1r
    
    x3=(bl-br)/(mr-ml)
    y3=ml*x3+bl
    
    
    #mm=(y3-k[0])/(x3-k[1]/2)
    
    
    #cv2.line(img,(int(x3),int(y3)),(k[1]/2,k[0]),(255,255,0),3)  
    #cv2.line(img,(k[1]/2,0),(k[1]/2,k[0]),(255,255,255),3)  
    
    
    me=ma.atan(mm)*180/np.pi  
    
    if me<85 :
        a='d'
        
    elif me>95:
            a='i'
            
    else:
            a='c'
    
    return a