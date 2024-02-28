import cv2
import numpy as np 

# AND , OR, NOT , XOR



img1 = np.zeros((400,400,3),np.uint8) # Blank Image

img1 = cv2.rectangle(img1,(150,100),(200,250),(255,255,255,255),-1) # white color filled rectangle

img2 = np.zeros((400,400,3),np.uint8) # Blank Image

img2 = cv2.rectangle(img2,(10,10),(170,190),(255,255,255,255),-1) # white color filled rectangle


bitAnd = cv2.bitwise_and(img2,img1)

bitOR = cv2.bitwise_or(img2,img1)

bitNot_1 = cv2.bitwise_not(img1)

bitNot_2 = cv2.bitwise_not(img2)

bitXOR = cv2.bitwise_xor(img2,img1)


l = cv2.add(img1,bitNot_2)
r = cv2.add(bitNot_1,img2)
bitXNOR = cv2.multiply(l,r)

cv2.imshow('Result_1',img1)
cv2.imshow('Result_2',img2)
cv2.imshow('Bitwise_And',bitAnd) # common portion 
cv2.imshow('Bitwise_OR',bitOR)
cv2.imshow('Bitwise_Not_1',bitNot_1)
cv2.imshow('Bitwise_Not_2',bitNot_2)
cv2.imshow('Biwise_XOR',bitXOR)
cv2.imshow('Bitwise_XNOR',bitXNOR)
cv2.imshow('Left',l)
cv2.imshow('Right',r)







cv2.waitKey(0)
cv2.destroyAllWindows()