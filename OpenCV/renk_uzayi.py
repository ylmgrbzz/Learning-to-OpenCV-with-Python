import cv2

img=cv2.imread("resim.jpg")

rgb_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("resimBGR",img)
cv2.imshow("resimRGB",rgb_img)
cv2.imshow("resimHSV",hsv_img)
cv2.imshow("resimGRAY",gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()