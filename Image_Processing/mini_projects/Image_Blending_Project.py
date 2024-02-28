import cv2 
import numpy as np 
img1 = cv2.imread('ImageProcessing_Operations/include/Nobita.jpg')
img1 = cv2.resize(img1,(300,300))
img2 = cv2.imread('ImageProcessing_Operations/include/multi_color.jpg')
img2 = cv2.resize(img2,(300,300))

def blend(x):
    pass


img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow('Blending_Project')

cv2.createTrackbar('Alpha','Blending_Project',1,100,blend)

switch = '0: OFF \n 1: ON' 
# create switch to invoke trackbar
cv2.createTrackbar(switch,'Blending_Project',0,1,blend)

while True:
    s = cv2.getTrackbarPos(switch,'Blending_Project')
    a = cv2.getTrackbarPos('Alpha','Blending_Project')
    n = float(a/100)
    #print(n)

    if s == 0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst,str(a),(20,50),cv2.FONT_ITALIC,2,(0,125,255),2)
    cv2.imshow('Blending_Project',dst)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cv2.destroyAllWindows()