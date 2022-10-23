import cv2
import numpy as np
img = cv2.imread('averaging.jpg')
blurred = cv2.blur(img,(5,5))
g_blurred = cv2.GaussianBlur(img, (7,7),0)

img1 = cv2.imread('median_blur.png')
median = cv2.medianBlur(img1, 7)



cv2.imshow('image1',img)
cv2.imshow('image2',blurred)
cv2.imshow('image3',g_blurred)
cv2.imshow('image4',median)

cv2.waitKey(0)
cv2.destroyAllWindows()