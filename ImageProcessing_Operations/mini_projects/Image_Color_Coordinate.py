import numpy as np 
import cv2

def mouse_event(event,x,y,flags,param):
    print("x==",x)
    print("y==",y)
    print("flags",flags)
    print("param",param)
    font = cv2.FONT_HERSHEY_PLAIN
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',' , y)

        cord = ". "+str(x)+ ', '+str(y)
        cv2.putText(img,cord,(x,y),font,1,(15,12,100),2)
        #cv2.imshow('image',img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y,x,0] # blue
        g = img[y,x,1] # green
        r = img[y,x,2] # red

        color_bgr = ". "+str(b)+ ', '+str(g) + ', '+str(r)
        cv2.putText(img,color_bgr,(x,y),font,1,(10,50,130),2)
        #cv2.imshow('image',img)
    
cv2.namedWindow(winname="output")

#img = np.zeros([512,512,3],np.uint8)
img = cv2.imread('ImageProcessing_Operations/include/Tiger.jpg')
cv2.setMouseCallback("output",mouse_event) # binding the mouse event

while True:
    cv2.imshow("output",img)
    k = cv2.waitKey(1) # holding waitkey to stop the vedio.
    if k == ord("q"): # if any addidtional error use mask = 0xFF , if k == ord("q") & 0xFF:
        break

cv2.destroyAllWindows()