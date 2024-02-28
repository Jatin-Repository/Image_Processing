import cv2

'''
IP Webcam Pro mobile access download.
Use IP Address for code.
Mobile and Deasktop connected to same network.

'''

camera = "http://192.168.253.237:8080/vedio"

cap = cv2.VideoCapture(0)# 0 if your primary camera, 1 for external webcam
print(cap)
cap.open(camera)

fourcc = cv2.VideoWriter.fourcc('X','V','I','D') # *"XVID" prefered

output = cv2.VideoWriter('ImageProcessing_Operations/include/output.avi',fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# taking frames size from vedio capture.
print("Output",output)
print(cap.isOpened())
while cap.isOpened(): # while camera is opened
    ret, frame = cap.read() # ret boolean value
    if ret == True: # frame is reading, TRue indicate new frame came.
        frame = cv2.resize(frame,(700,450))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        cv2.imshow("gray",gray)
        #output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
cap.release()
cv2.destroyAllWindows() 