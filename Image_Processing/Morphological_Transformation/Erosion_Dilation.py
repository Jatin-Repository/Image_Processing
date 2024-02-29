import cv2 
import numpy as np 

# img = cv2.imread('Image_Processing/include/Multi_Color_Balls.jpg')

img = cv2.imread('Image_Processing/include/Ball_Colorfull.jpg',0) # dirdctly in greayscale
img = cv2.resize(img,(200,200))
_,mask = cv2.threshold(img,190,255,cv2.THRESH_BINARY_INV)

#Kaernel Creation

black_kernel = np.ones((5,5),np.uint8)# 5x5 kernel with full of ones.
#white_kernel = np.ones((5,5),np.uint8)*255


cv2.imshow('Resullt',img)
cv2.imshow('Simple Thresholding',mask)
cv2.imshow('Black_Kernel',black_kernel)
#cv2.imshow('White_Kernel',white_kernel)


# Erosion
errosion = cv2.erode(mask,black_kernel)

cv2.imshow('Errosion',errosion)

kernel_1 = np.ones((1,1),np.uint8) # 5x5 with full ones
dilation_1 = cv2.dilate(mask,kernel_1) #iteration is optional


cv2.imshow("Kernal for Dilation(1x1)",kernel_1)

cv2.imshow("Dilate-1",dilation_1)


kernel_2 = np.ones((3,3),np.uint8) # 5x5 with full ones
dilation_2 = cv2.dilate(mask,kernel_2) #iteration is optional


cv2.imshow("Kernal for Dilation(3x3)",kernel_2)

cv2.imshow("Dilate-2",dilation_2)

cv2.waitKey(0)
cv2.destroyAllWindows()