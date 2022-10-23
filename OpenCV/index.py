import cv2

img=cv2.imread("resim.jpg",0)
cv2.imwrite("resim1.jpg",img)

cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()