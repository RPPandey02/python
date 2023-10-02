# using cv we pop a window too
import cv2
vid=cv2.VideoCapture("E:\\vscode\\python\\video sample.mp4")
while(vid.isOpened()):
    ret,frame=vid.read()
    if ret==True:
        cv2.imshow("frame",frame)
        if cv2.waitKey(25) & 0xFF == ord('x'):
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()

