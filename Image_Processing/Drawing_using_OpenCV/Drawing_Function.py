import cv2
import numpy as np 
img  = cv2.imread('ImageProcessing_Operations/include/Tom_Jerry.jpg')

cv2.imshow("result",img)
cv2.resize(img,(600,700))
img = cv2.line(img,(0,0),(200,200), (154,92,424), 5) #color format BGR
'''((a,b),(c,d),(e,f,g),h) (a,b) and (c,d) are end point of line,
 where (e,f,g) are color code (blue,green,red) 
and h is thickness.
'''

img = cv2.arrowedLine(img,(600,150),(200,100), (100,92,424), 10)


img = cv2.rectangle(img,(384,10),(510,128),(128,0,255),7)


img = cv2.rectangle(img,(700,10),(650,285),(128,0,120),-1) #to fill

img = cv2.circle(img,(447,255),63,(214,255,0),-5)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'Hi', (20,500),font,4,(0,125,255),10,cv2.LINE_AA)

img = cv2.ellipse(img,(500,300),(200,50),10,10,270,25,5)

cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()