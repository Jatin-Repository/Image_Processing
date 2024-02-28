import numpy as np 
import cv2 

# read
img = cv2.imread('ImageProcessing_Operations/include/Tiger.jpg')
img = cv2.resize(img,(800,500)) # width,height

# ROI(Region of Intrest)
# (318,79),(),(),(490,229) prinicapal diagonal key end point hen.

# pass [(y1:y2),(x1,x2)] format 
# y_diff = 150 x_diff = 172
roi = img[79:229,318:490] # head of lion

# now passing data to image
img[79:229,491:663] = roi

img[79:229,145:317] = roi

# changing y axis

img[300:450,0:172]= roi

cv2.imshow("Region of Intrest",roi)
cv2.imshow("Result",img)

cv2.waitKey(0)
cv2.destroyAllWindows()