# simple thresholding(img,pixel_thresh,_max_thresh_pixel,style)

import cv2
import numpy as np 

img = cv2.imread('Image_Processing/include/Black_White.jpg')
img = cv2.resize(img,(300,200))
cv2.imshow("Original Image",img)

_, th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY) # >50 == 1 <50 == 0
# a, th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY) # >50 == 1 <50 == 0

# print(a) thresold value
cv2.imshow("1 - THRESH_BINARY",th1)

_, th2 = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV) # >50 == 1 <50 == 0

cv2.imshow("2 - THRESH_BINARY_INV",th2)

_, th3 = cv2.threshold(img,120,255,cv2.THRESH_TRUNC) # >50 == 1 <50 == 0

cv2.imshow("3 - THRESH_TRUNC",th3) # jo last value miley usa spread kar diya remaining data par.


_, th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) # after zero jo value miley usa spread kar diya.

cv2.imshow("4 - THRESH_TOZERO",th4)

_, th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) # after zero jo value miley usa spread kar diya.

cv2.imshow("5 - THRESH_TOZERO_INV",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
