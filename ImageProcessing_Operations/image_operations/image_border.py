# create Image Border
# using cv2.copyMakeBorder() function.
#it take paramter like(img,border_width(4-sides),bordertype,val_border) val_border is for color
#border width = top,bottom,right,left



import cv2 
import numpy

img1 = cv2.imread('ImageProcessing_Operations/include/Nobita.jpg')
img1 = cv2.resize(img1,(250,250))

# creating image border
border = cv2.copyMakeBorder(img1,10,10,5,5,cv2.BORDER_CONSTANT, value=[255,0,125]) # value for color

cv2.imshow("output",border)
cv2.waitKey(0)
cv2.destroyAllWindows()