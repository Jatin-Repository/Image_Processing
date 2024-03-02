import cv2
import numpy as np

img = cv2.imread('Image_Processing/include/noisy2.jpg')
img = cv2.resize(img,(200,200))
cv2.imshow("Blur_Image",img)


kernel_1 = np.ones((5,5),np.float32)/16
# Homogenous Filter
h_filter_1 = cv2.filter2D(img,-1,kernel_1) # -1 is desired path

#h_filter_2 = cv2.filter2D(img,-2,kernel) # -1 is desired path

cv2.imshow("Kernal",kernel_1)
cv2.imshow("Homogenous Filter-1",h_filter_1)
#cv2.imshow("Homogenous Filter-2",h_filter_2)

#Blur(Averaging)
blur = cv2.blur(img,(5,5))
cv2.imshow("Bluring(Average)",blur)


#Gaussian Filter

gaussian = cv2.GaussianBlur(img,(5,5),0) #here 0 is sigma x value
cv2.imshow("Gaussian Blur",gaussian)

#Median Filter
median = cv2.medianBlur(img,5)
cv2.imshow("Median Filter",median)


#Bilateral Filter
bi_f = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("Bilateral Filter",bi_f)

cv2.waitKey(0)
cv2.destoryAllWindows()
