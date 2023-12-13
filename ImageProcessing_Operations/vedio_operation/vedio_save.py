import cv2


cap = cv2.VideoCapture(0)# 0 if your primary camera, 1 for external webcam
print(cap)
# Creating Container and wriring with help of Vedio Writer

# For saving vedio format DIVX,XVID,MJPG,X264,WMVI,WMV2

fourcc = cv2.VideoWriter.fourcc('X','V','I','D') # *"XVID" prefered

print('fourcc:',fourcc)

# fourcc help vedio witer as to which format vedio nedd to store and XVID is highly prefered.

# It contain 4 parameter , name,codec,fps,resolution


#output = cv2.VideoWriter("ImageProcessing_Operations/include/vediography.avi",cv2.VideoWriter.fourcc('X','V','I','D'),20.0,(640,280),1)
output = cv2.VideoWriter('ImageProcessing_Operations/include/output.avi',fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
output1 = cv2.VideoWriter('ImageProcessing_Operations/include/output_bw.avi',fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# taking frames size from vedio capture.
print("Output",output)


while cap.isOpened(): # while camera is opened
    ret, frame = cap.read() # ret boolean value
    if ret == True: # frame is reading, TRue indicate new frame came.
        # frame = cv2.resize(frame,(700,450))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        bgr_img = cv2.cvtColor(gray, cv2.COLOR_RGB2BGR)
        cv2.imshow('frame',frame)
        cv2.imshow("gray",gray)
        output.write(frame)
        output1.write(bgr_img)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
print(output)
cap.release()
output.release() # if not done vedio might get corrupted.
output1.release()

cv2.destroyAllWindows() 