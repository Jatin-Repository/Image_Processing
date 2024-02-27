import numpy as np 
import cv2 

img = np.zeros([512,512,3],np.uint8)*255 # Foer Black Image

img1 = np.ones([512,512,3],np.uint8)*255  # For White Image

cv2.imshow("Black",img)
cv2.imshow("White",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()