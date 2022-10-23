import cv2
import numpy as np
import matplotlib.pyplot as plt

x=np.uint8([120])
y=np.uint8([25])

z=cv2.add(x,y)

print(z)

img1=np.zeros((300,300,3),np.uint8)+255
cv2.circle(img1,(150,150),50,(255,0,0),-1)
cv2.imshow("img1",img1)

img2=np.zeros((300,300,3),np.uint8)+255
cv2.line(img2,(0,0),(300,300),(0,255,0),5)
cv2.imshow("img2",img2)

dst=cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow("dst",dst)
cv2.waitKey(0)

img11 = np.zeros((400,400), np.uint8)
white = (255,255,255)
cv2.rectangle(img11, (75,75), (325,325), white, -1)
cv2.imshow("Rectangle",img11)
img22 = np.zeros((400,400), np.uint8)
cv2.circle(img22, (200,200), 175, white, -1)
cv2.imshow("Circle",img22)
cv2.waitKey(0)
cv2.destroyAllWindows()

bitwiseAnd = cv2.bitwise_and(img1, img2)
bitwiseOr = cv2.bitwise_or(img1,img2)
bitwiseXor = cv2.bitwise_xor(img1, img2)
bitwiseNot = cv2.bitwise_not(img2)

titles = ["Rectangle", "Circle", "Bitwise And", "Bitwise Or", "Bitwise Xor", "Bitwise Not"]
images = [img1, img2, bitwiseAnd, bitwiseOr, bitwiseXor, bitwiseNot]
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(cv2.cvtColor(images[i],cv2.COLOR_RGB2BGR))
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()