import cv2
import numpy as np

frame = cv2.imread('Image_Processing/include/Multi_Color_Balls.jpg')
#frame = cv2.imread('ImageProcessing_Operations/include/multi_color.jpg')
#cv2.imshow('Original_Result',frame)
frame = cv2.resize(frame,(300,300))

def nothing(x):
    pass

cv2.namedWindow("Dynamic Color Picker")

cv2.createTrackbar('Lower_H',"Dynamic Color Picker", 0, 255, nothing)
cv2.createTrackbar('Lower_S',"Dynamic Color Picker", 0, 255, nothing)
cv2.createTrackbar('Lower_V',"Dynamic Color Picker", 0, 255, nothing)

cv2.createTrackbar('Upper_H',"Dynamic Color Picker", 255, 255, nothing)
cv2.createTrackbar('Upper_S',"Dynamic Color Picker", 255, 255, nothing)
cv2.createTrackbar('Upper_V',"Dynamic Color Picker", 255, 255, nothing)


while True:
    hsv  = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower_H","Dynamic Color Picker")
    l_s = cv2.getTrackbarPos("Lower_S","Dynamic Color Picker")
    l_v = cv2.getTrackbarPos("Lower_V","Dynamic Color Picker")


    h_h = cv2.getTrackbarPos("Upper_H","Dynamic Color Picker")
    h_s = cv2.getTrackbarPos("Upper_S","Dynamic Color Picker")
    h_v = cv2.getTrackbarPos("Upper_V","Dynamic Color Picker")

    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([h_h,h_s,h_v])

    mask = cv2.inRange(hsv,lower_bound,upper_bound)

    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('Dynamic Color Picker',frame)
    cv2.imshow('Masking_Result',mask)
    cv2.imshow("Output",result)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cv2.destroyAllWindows()




