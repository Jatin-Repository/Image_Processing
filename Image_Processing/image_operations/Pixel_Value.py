import numpy as np 
import cv2

#Read an Image
img = cv2.imread('ImageProcessing_Operations/include/multi_color.jpg')
#img = cv2.resize(img,(250,250))
print("shape==",img.shape) # return tuple of number of rows columns and channel.
print("no of pixels==",img.size) # number of pixel
print("datatype==",img.dtype) # return Image datatype
print("Imagetype==",type(img))

px = img[520,580] # store value at x = 520 and y = 580 , color [b,g,r]
print("The color pixel coordinate ==",px) # we get the pixel.

# channel default value blue =0, grren=1, red=2
# accing only blue pixel.

blue = img[520,580,0]
print("the pixel having blue color==",blue)

green = img[520,580,1] # for green pass 1
print("The pixel having green color==",green)

red = img[520,580,2]
print("The pixel having red color==",red)

cv2.waitKey(0)
cv2.destroyAllWindows()