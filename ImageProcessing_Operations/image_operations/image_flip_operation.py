import cv2

'''
if unicode error to resolve
1. use double back slash instaed of single.
2. or use r'' before file path.

'''
path = 'ImageProcessing_Operations/include/Alphabet_B.jpg'


#read image
img1 = cv2.imread(path,0) # convert image to balcak and white
img1 = cv2.resize(img1,(560,500))
cv2.imshow("original image:",img1)

img2 = cv2.imread(path,0) 
img2 = cv2.resize(img2,(560,500))
img2 = cv2.flip(img2,0)
cv2.imshow("Fliped Horizontally image:",img2)

img3 = cv2.imread(path,0) 
img3 = cv2.resize(img3,(560,500))
img3 = cv2.flip(img3,1)
cv2.imshow("Fliped Vertically image:",img3)

img3 = cv2.imread(path,0) 
img3 = cv2.resize(img3,(560,500))
img3 = cv2.flip(img3,-1)
cv2.imshow("Fliped Downward and then Vertically image:",img3)
cv2.waitKey(0)

cv2.destroyAllWindows()