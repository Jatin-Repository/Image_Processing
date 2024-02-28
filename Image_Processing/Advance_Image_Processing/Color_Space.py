# In Open CV more than 150 color spaces exist. One among is HSV (Heu Saturation Value)

# Color Intensity and Color Inormation seprate using HSV.

import numpy as np 
import cv2

frame = cv2.imread('ImageProcessing_Operations/include/Multi_Color_Balls.jpg')
#frame = cv2.imread('ImageProcessing_Operations/include/multi_color.jpg')
#cv2.imshow('Original_Result',frame)
frame = cv2.resize(frame,(300,300))

while True:
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    u_v = np.array([17,237,226]) # (b,g,r) 226, 237, 17
    l_v = np.array([12,199,190]) # 190, 199, 12
    # Creating Mask to detect specific color.
    mask = cv2.inRange(hsv, l_v, u_v)
    
    #Filter the pixel in image
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('Original_Result',frame)
    cv2.imshow('Masking Image',mask)
    cv2.imshow('Final_Result',res)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cv2.destroyAllWindows()