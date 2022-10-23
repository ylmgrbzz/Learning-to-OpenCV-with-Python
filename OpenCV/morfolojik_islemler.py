import cv2
import numpy as np

img = cv2.imread('erosion.png')

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 3)
cv2.imshow("Erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('dilation.png')

dilation = cv2.dilate(img,kernel,iterations = 15)
cv2.imshow("dilation image", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('opening.png',0)
kernel = np.ones((7,7),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.imread('closing.png',0)
kernel = np.ones((7,7),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()