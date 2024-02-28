import cv2

cap = cv2.VideoCapture("ImageProcessing_Operations/include/Tom and Jerry - Professor Tom.mp4") 
# to captue vedio and store object.
# vedio is collection of image
print('Vedio:',cap)

while(True): #it will run it all frame is not completed, frocefully we need to terminate code.
    ret,frame = cap.read() # ret is boolean variable and image is in frame
    frame = cv2.resize(frame,(700,450)) # (width,height)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#black-white vedio
    cv2.imshow("frame",frame)
    cv2.imshow("gary_scale",gray)
    k = cv2.waitKey(25) # holding waitkey to stop the vedio.
    # waitkey valuer smaller indicate fast frame view, if more will take long time to get the next frame.
    if k == ord("q"): # if any addidtional error use mask = 0xFF , if k == ord("q") & 0xFF:
        break

cap.release() # releasing the vedio.
cv2.destroyAllWindows()