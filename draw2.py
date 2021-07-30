import cv2
import numpy as np


def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        boxes[0]=(x,y)
        line.append((x,y))
    if event == cv2.EVENT_LBUTTONUP:
        cv2.line(imga,boxes[0],(x,y),(255,0,0),3)
        line.append((x,y))

if __name__ == "__main__":
    boxes=[1]
    line=[]
    vedio_path = r"C:\Users\simon\Desktop\track3.7_windows/test.mp4"
    cap = cv2.VideoCapture(vedio_path)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 2);
    cap.set(3, 1920)
    cap.set(4, 1080)
    cv2.namedWindow('img',0)
    cv2.resizeWindow('img',900,900)
    cv2.setMouseCallback('img',draw)
    while 1:
        ret,frame_read = cap.read()
        imga = frame_read
        imga = cv2.resize(imga,(608,608))
        while(1):
            cv2.imshow('img',imga)
            if cv2.waitKey(20) & 0xFF == 27:
                break
        np.savetxt("line.txt",line,fmt='%1.4e')
        break