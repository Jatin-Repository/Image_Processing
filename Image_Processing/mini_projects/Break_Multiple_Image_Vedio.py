import cv2

vidcap = cv2.VideoCapture('ImageProcessing_Operations/include/TomandJerry.avi')
print(vidcap)
ret,image = vidcap.read() # Read the vedio
count = 0

## Single Frame ko read karenga
# while True:
#     if ret == True:
#         cv2.imshow("res",image)

#         count += 1
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#             cv2.destroyAllWindows()


if ret == True:
        while ret:
            ret,image = vidcap.read()
            #cv2.imshow("res",image)
            cv2.imwrite("ImageProcessing_Operations/include/Frames/ImageN%d.jpg"%count,image)
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)) # speed of vedio capture
            # ret,image = vidcap.read()
            cv2.imshow("res",image)

            count += 1
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            
vidcap.release()
cv2.destroyAllWindows()
