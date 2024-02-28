import numpy as np 
import cv2
import datetime
cap = cv2.VideoCapture('ImageProcessing_Operations/include/Tom and Jerry - Professor Tom.mp4')# 0 if your primary camera, 1 for external webcam

#cap = cv2.VideoCapture(0)# 0 if your primary camera, 1 for external webcam


print("for width===",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for height===",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

'''
print("for width===",cap.get(3))
print("for height===",cap.get(4))

'''

while cap.isOpened(): # while camera is opened
    ret, frame = cap.read() # ret boolean value
    if ret == True: # frame is reading, True indicate new frame came.
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = 'Height:' + str(cap.get(4)) + ' Width: '+str(cap.get(3))
        frame = cv2.putText(frame,text,(10,20),font,1,(0,155,255) , 1, cv2.LINE_AA)

        date_data = "Date: "+ str(datetime.datetime.now())
        frame = cv2.putText(frame, date_data,(20,50), font,1, (100,255,255),1,cv2.LINE_AA)

        frame = cv2.resize(frame,(700,450))
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        #cv2.imshow("gray",gray)

        # k = cv2.waitKey(100)
        # if k == ord("q") & 0xFF:
        #     break

        # dircetly
        if cv2.waitKey(30) & 0xFF == ord('q'):  # 30 millisecond frame will be loaded.
            break
    else:
        break
cap.release()
cv2.destroyAllWindows() 