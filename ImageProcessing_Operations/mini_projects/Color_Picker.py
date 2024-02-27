import numpy as np 
import cv2

def cross(x):
    pass



img = np.zeros((255,255,3),np.uint8)

cv2.namedWindow("Color Picker",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Picker", 700, 1020) 

# Create Switch
s1 = "0:OFF\n1:ON"
cv2.createTrackbar(s1,"Color Picker",0,1,cross)


#creating for rgb, default will use cross
cv2.createTrackbar("R","Color Picker",0,255,cross)
cv2.createTrackbar("G","Color Picker",0,255,cross)
cv2.createTrackbar("B","Color Picker",0,255,cross)


while True:
    cv2.imshow("Color Picker",img)
    k = cv2.waitKey(1) # holding waitkey to stop the vedio.
    if k == ord("q"): # if any addidtional error use mask = 0xFF , if k == ord("q") & 0xFF:
        break


    # now get tracbar position
    s = cv2.getTrackbarPos(s1,"Color Picker")
    r = cv2.getTrackbarPos("R","Color Picker")
    g = cv2.getTrackbarPos("G","Color Picker")
    b = cv2.getTrackbarPos("B","Color Picker")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [r,g,b]

cv2.destroyAllWindows()