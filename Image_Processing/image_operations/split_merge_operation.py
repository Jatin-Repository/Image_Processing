import numpy as np 
import cv2

#Read an Image
img = cv2.imread('ImageProcessing_Operations/include/Nobita.jpg')
img = cv2.resize(img,(250,250))
print("shape==",img.shape) # return tuple of number of rows columns and channel.
print("no of pixels==",img.size) # number of pixel
print("datatype==",img.dtype) # return Image datatype
print("Imagetype==",type(img))


# split - return 3 channel for your image which is blue green red as per open cv.
#print(cv2.split(img))

b,g,r = cv2.split(img)

# cv2.imshow("blue",b)
# cv2.imshow("green",g)
# cv2.imshow("red",r)

merge1 = cv2.merge((r,g,b))

merge2 = cv2.merge((b,g,r)) # open cv follow.

merge3 = cv2.merge((g,b,r))


cv2.imshow("merge1",merge1)
cv2.imshow("merge2",merge2)
cv2.imshow("merge3",merge3)
cv2.imshow("original",img)

#cv2.imshow("Result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()