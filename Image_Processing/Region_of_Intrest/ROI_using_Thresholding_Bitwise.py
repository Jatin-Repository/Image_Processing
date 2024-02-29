import numpy as np 
import cv2 

# read
img1 = cv2.imread('Image_Processing/include/Tiger.jpg')
img1 = cv2.resize(img1,(1080,720)) # width,height

img2 = cv2.imread('Image_Processing/include/Superman.jpeg')
img2 = cv2.resize(img2,(500,500)) # width,height

# img2 will be smaller than or equal to img1

cv2.imshow("Image-1",img1)
cv2.imshow("Image-2",img2)

r,c,ch = img2.shape
print(r,c,ch)

roi = img1[0:r,0:c]

#cv2.imshow("ROI",roi)

# Thresholding is performed if image is in Greyscale.
img_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#masking == thresolding

_,th = cv2.threshold(img_gray,50,255, cv2.THRESH_BINARY)

#remove background
mask_inv = cv2.bitwise_not(th)

#put mask on the roi
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

#Take only region of figure from original image
img2_fg = cv2.bitwise_and(img2,img2,mask=th)


#put mask on the roi
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

#Take only region of figure from original image
img2_bg = cv2.bitwise_and(img2,img2,mask=th)

#put logo in ROI in the main image
result = cv2.add(img1_bg,img2_fg)

final = img1

final[0:r,0:c]=result

cv2.imshow("Step 1 = Gray Scale Image",img_gray)

cv2.imshow("Step 2 = Mask",th)

cv2.imshow('Step 3 = Mask_inv',mask_inv)

cv2.imshow('Step 4 = Mask Figure Foreground',img1_bg)

cv2.imshow('Step 5 = Mask Figure Background',img2_bg)

cv2.imshow('Step 6 = Result',result)

cv2.imshow("Step 7 = Final",final)

cv2.waitKey(0)
cv2.destroyAllWindows()