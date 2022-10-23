import cv2

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
fileName="C:\Users\yalim\PycharmProjects\opencv\output.avi"
codec=cv2.VideoWriter_fourcc("W","M","V","2")
videoFileOutput=cv2.VideoWriter(fileName,codec,30,(640,480))
while 1:
    ret, frame=cap.read()
    videoFileOutput.write(frame)

    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Webcam",frame)
    cv2.imshow("Webcam1",gray)

    if cv2.waitKey(1) == 27:
        break

cap.release()
videoFileOutput.release()
cv2.destroyAllWindows()