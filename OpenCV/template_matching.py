import cv2 as cv
import numpy as np
src=cv.imread("opencv1.png")
tpl=cv.imread("opencv2.PNG")

cv.imshow("input",src)
cv.imshow("tpl",tpl)

th,tw=tpl.shape[:2]
result=cv.matchTemplate(src,tpl,method=cv.TM_CCORR_NORMED)
cv.imshow("result",result)

t=0.98
loc=np.where(result> t)

for pt in zip(*loc[::-1]):
    cv.rectangle(src,pt,(pt[0]+tw,pt[1]+th),(255,0,0),1,8,0)

cv.imshow("ylm",src)
cv.waitKey(0)