import cv2
import numpy as np
img = cv2.imread("resim.jpg")

color = img[150, 200]
print(color)

blue = img[150,200,0]
print(blue)

img[150,200,0] = 250
print(img[150,200,0])

blue = img.item(150,200,0)
print(blue)

img.itemset((150,200,0),250)
print(img[150,200,0])

shape = img.shape
print(shape )

face= img[30:200, 200:400]
cv2.imshow("ROI",face)
cv2.waitKey(0)
cv2.destroyAllWindows()