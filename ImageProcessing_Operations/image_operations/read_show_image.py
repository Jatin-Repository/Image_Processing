'''
 A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python virtual environments for them.
 This is one of the most important tools that most Python developers use.

 Create virtual environment : python3 -m venv env_name
 Activate: source Image_Processing_Operations/bin/activate

 Open Cv comes with BGR , but we hear RGB(widely).

 waitKey(x): It is used to control the image or less it it blink and goes off, 
 x(msec) indicate time for which you want to hold the image display window.

 destroyAllWindows(): It will remove all accquire space by ide to get release.
'''

import cv2

img1 = cv2.imread('ImageProcessing_Operations/include/Tiger.jpg',1) # 1 colorfull
print(img1) #numpy array of pixel

img1 = cv2.resize(img1,(1200,500)) #(width,height)
cv2.imshow("original",img1)


## GrayScale image
img2 = cv2.imread('ImageProcessing_Operations/include/Tiger.jpg',0) # 1 colorless
print('Gray Scale Image',img2) #numpy array of pixel

img2= cv2.resize(img2,(1200,500)) #(width,height)
cv2.imshow("Updated",img2)

## Unchanged : Load image such as including alpha channels.
img3 = cv2.imread('ImageProcessing_Operations/include/Tiger.jpg',-1) # -1 unchanged, intensity of color increase.
print('Color Intensity Increased Original Image',img3) #numpy array of pixel

img3= cv2.resize(img3,(1200,500)) #(width,height)
cv2.imshow("Unchanged",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()