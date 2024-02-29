# data loss is very high with simple threshold.
import numpy as np 
import cv2 

img = cv2.imread('Image_Processing/include/Black_White.jpg')
img = cv2.resize(img,(300,200))

'''
THis error is 
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) # 11 ka group for phir mean
cv2.error: OpenCV(4.8.1) /io/opencv/modules/imgproc/src/thresh.cpp:1674: error: (-215:Assertion failed) src.type() == CV_8UC1 in function 'adaptiveThreshold'
'''
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

cv2.imshow("Original Image",img)

_, th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY) # >50 == 1 <50 == 0 (data loss use adaptive)

cv2.imshow("Simple Thresholding",th1)


th2 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2) # 11 ka group for phir mean
# Adaptive will not return threshold value.
cv2.imshow("Adaptive Thresholding (MEAN)",th2)
# Note block size % 2 == 1 and blocksize > 1.
th3 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,2) # 11 ka group for phir mean
cv2.imshow("Adaptive Thresholding (Gaussian)",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()

