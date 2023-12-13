import cv2


cap = cv2.VideoCapture(0)# 0 if your primary camera, 1 for external webcam


while cap.isOpened(): # while camera is opened
    ret, frame = cap.read() # ret boolean value
    if ret == True: # frame is reading, TRue indicate new frame came.
        frame = cv2.resize(frame,(700,450))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        cv2.imshow("gray",gray)

        # k = cv2.waitKey(100)
        # if k == ord("q") & 0xFF:
        #     break

        # dircetly
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
cap.release()
cv2.destroyAllWindows() 