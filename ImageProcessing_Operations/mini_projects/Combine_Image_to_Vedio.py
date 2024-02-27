import cv2
import numpy as np
import os


height = 1280
width = 720
channel = 3

fps = 30
sec = 5
# choose codec according to format needed

fourcc = cv2.VideoWriter.fourcc('M','P','4','2')
video = cv2.VideoWriter('ImageProcessing_Operations/include/video_mix.avi', fourcc, float(fps), (width, height))

for frame_count in range(fps*sec):
    #img = np.random.randint(0,100 , (height,width,channel), dtype=np.uint8) random vedio
    path = f'ImageProcessing_Operations/include/Frames/ImageN{frame_count}.jpg'
    print(path)
    img =  cv2.imread(path)
    print(img)
    #print(frame_count)
    video.write(img)

video.release()
cv2.destroyAllWindows()
