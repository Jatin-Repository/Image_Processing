import cv2

'''
if unicode error to resolve
1. use double back slash instaed of single.
2. or use r'' before file path.

'''
path = input("Enter the Path and anme of image:")
print("Your Enter path is:",path)

#read image
img1 = cv2.imread(path,0) # convert image to balcak and white
img1 = cv2.resize(img1,(560,500))
cv2.imshow("converted image:",img1)


## To save hold waitKey() as it control the image

k = cv2.waitKey(0)
if k == ord("s"): # on pressing s key will save the image.
    cv2.imwrite("ImageProcessing_Operations/include/output.png",img1)
else:
    cv2.destroyAllWindows()