# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:19:23 2015

@author: jorge
"""

def lines_detect(rho,theta,randl,ranul,randr,ranur):
    
    T=[]
    R=[]
    RR=[]
    TR=[]
    TH=[]
    RH=[]
    RL=[]
    TL=[]
    
    for rho,theta in lines[0]:
        
        T.append(theta)
        R.append(rho)
            
        limdr=35*np.pi/180
        limur=75*np.pi/180
        
        if ((theta >=limdr) and (theta <=limur)): 
            
            TR.append(theta)
            RR.append(rho)
        
        limdl=115*np.pi/180
        limul=145*np.pi/180
        
        if ((theta >=limdl) and (theta <= limul)): 
        
            TL.append(theta)
            RL.append(rho)
        
        limhd=110
        limhu=165
        
        if (((theta>=0) and (theta <= limhd))) or (((theta >=limhu) and (theta <= 180))): 
        
            TH.append(theta)
            RH.append(rho)
            


    #----------------------------LEFT-------------------------------
    
    if ((not TL) or (not RL)):
        
        theta2=theta2a  
        
    else: 
          
            theta2=np.mean(TL)
            rho2=np.mean(RL) 
    
            ar = np.cos(theta2)
            br = np.sin(theta2)
            x0r = ar*rho2
            y0r = br*rho2
    
    
            x1r = int(x0r + 5000*(-br))
            y1r = int(y0r + 5000*(ar))
            x2r = int(x0r - 5000*(-br))
            y2r = int(y0r - 5000*(ar))
            theta2a=theta2
    
            
            cv2.line(img,(int(x1r),int(y1r)),(x2r,y2r),(0,0,255),3)         
    
    
            
    #-------------------------control--------------------
                
    #-------------------------RIGHT---------------------------------
    
    if ((not RR) or (not TR)):
          
          theta1=theta1a
    
    else:
          
            theta1=np.mean(TR)
            rho1=np.mean(RR)        
    
            al = np.cos(theta1)
            bl = np.sin(theta1)
            x0l = al*rho1
            y0l = bl*rho1
    
            x1l = int(x0l + 10000*(-bl))
            y1l = int(y0l + 10000*(al))
            x2l = int(x0l - 10000*(-bl))
            y2l = int(y0l - 10000*(al))
            
            theta1a=theta1
    
            cv2.line(img,(int(x1l),int(y1l)),(x2l,y2l),(255,0,0),3)     
    #-----------------------------CENTER-----------------------------
        
    if ((not RH) or (not TH)):
          
          theta3=theta3a
    else:
          
            theta3=np.mean(TH)
            rho3=np.mean(RH)        
    
            ah = np.cos(theta3)
            bh = np.sin(theta3)
            x0h = al*rho1
            y0h = bl*rho1
    
            x1h = int(x0h + 1000*(-bh))
            y1h = int(y0h + 1000*(ah))
            x2h = int(x0h - 1000*(-bh))
            y2h = int(y0h - 1000*(ah))
            
            theta3a=theta3
            
            #cv2.line(img,(int(x1h),int(y1h)),(x2h,y2h),(255,0,255),3)  
            
    return 0
