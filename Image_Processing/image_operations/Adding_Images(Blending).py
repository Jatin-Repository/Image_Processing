# Blending means adding two images.


import cv2 
import numpy as np 
img1 = cv2.imread('ImageProcessing_Operations/include/Nobita.jpg')
img1 = cv2.resize(img1,(300,300))
img2 = cv2.imread('ImageProcessing_Operations/include/multi_color.jpg')
img2 = cv2.resize(img2,(300,300))

# Note: Blending can be perfrom only on same size of image.

result1 = np.add(img1,img2) # not blending
result2 = img1+img2  # not Blending
# result3 = img2+img1 same as result2
result3 = cv2.add(img1,img2) # pixel addition and then mean to it.
cv2.imshow('Image_1',img1)
cv2.imshow('Image_2',img2)
#cv2.imshow('Adding Images',result1)
cv2.imshow('Simple Adding 1st and 2nd image',result2)
cv2.imshow('Blending of two Image',result3)

# fuction cv2.addWeighted(img1,wt1,img2,wt2,gama_val) # gama_val = color saturation value.
result4 = cv2.addWeighted(img1,0.7,img2,0.3,0) # sum should be one 0.7+0.3=1
cv2.imshow('Weighted(Img1>Img2) Blending of two Image',result4)

result5 = cv2.addWeighted(img1,0.3,img2,0.7,0) # sum should be one 0.7+0.3=1
cv2.imshow('Weighted Blending(Img2>Img1) of two Image',result5)

result6 = cv2.addWeighted(img1,0.5,img2,0.5,0) # sum should be one 0.7+0.3=1
cv2.imshow('Weighted Blending(Img2=Img1,gama=0) of two Image',result6)

result7 = cv2.addWeighted(img1,0.5,img2,0.5,1) # sum should be one 0.7+0.3=1
cv2.imshow('Weighted Blending(Img2=Img1,gama=1) of two Image',result6)

result8 = cv2.addWeighted(img1,0.5,img2,0.5,2) # sum should be one 0.7+0.3=1
cv2.imshow('Weighted Blending(Img2=Img1,gama=2) of two Image',result6)

result9 = cv2.addWeighted(img1,0.5,img2,0.5,3) # sum should be one 0.7+0.3=1
cv2.imshow('Weighted Blending(Img2=Img1, gama=3) of two Image',result6)

cv2.waitKey(0)
cv2.destroyAllWindows()
