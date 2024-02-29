import cv2 
import numpy as np 
from matplotlib import pyplot as plt

# img = cv2.imread('Image_Processing/include/Multi_Color_Balls.jpg')

img = cv2.imread('Image_Processing/include/Ball_Colorfull.jpg',0) # dirdctly in greayscale
img = cv2.resize(img,(200,200))
_,mask = cv2.threshold(img,190,255,cv2.THRESH_BINARY_INV)

#Kaernel Creation

black_kernel = np.ones((5,5),np.uint8)# 5x5 kernel with full of ones.
#white_kernel = np.ones((5,5),np.uint8)*255

# Erosion
errosion = cv2.erode(mask,black_kernel)



kernel_1 = np.ones((1,1),np.uint8) # 5x5 with full ones
dilation_1 = cv2.dilate(mask,kernel_1) #iteration is optional


kernel_2 = np.ones((3,3),np.uint8) # 5x5 with full ones
dilation_2 = cv2.dilate(mask,kernel_2) #iteration is optional

titles = ["image","black_kernel","erosion","dilation-1","dilation-2"]
images = [img,black_kernel,errosion,dilation_1,dilation_2]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'Gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()


# cv2.waitKey(0)
# cv2.destroyAllWindows()