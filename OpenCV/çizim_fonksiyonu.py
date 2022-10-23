import cv2
import numpy as np

canvas= np.zeros((512,512,3),dtype=np.uint8)+255
print(canvas)

cv2.line(canvas,(0,10),(512,512),(255,0,0),5)
cv2.rectangle(canvas,(150,150),(320,320),(0,250,0),-1)
cv2.circle(canvas,(150,150),50,(0,0,255),-1)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas,"Yalim Gurbuz",(10,100),font,1,(245,158,66),4,cv2.LINE_AA)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()