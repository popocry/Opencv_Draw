# -*- coding: utf-8 -*-
'''
Created on 2018-8-25 20:07:44
@author: skyblue
'''
import cv2
import numpy as np
 
# -----------------------鼠标操作相关------------------------------------------
tpPointsChoose = []
pointsCount = 0
pointsMax = 4
def on_mouse(event, x, y, flags, param):
    global img, point1, point2, count, pointsMax
    global tpPointsChoose  # 存入選擇的點
    global pointsCount  # 對滑鼠按下的計數
    global img2
    img2 = img.copy()  # 此行代碼保證每次都重新在原圖畫，避免畫多了
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        pointsCount = pointsCount + 1
        print('pointsCount:', pointsCount)
        point1 = (x, y)
        print (x, y)
        # 畫出點擊的點
        cv2.circle(img2, point1, 10, (0, 0, 255), 2)
        # 將選擇的點保存到listlist列表裡
        tpPointsChoose.append((x, y))  # 用於畫點
        # ----------------------------------------------------------------------
        # 將畫的點兩兩相連起來
        print(len(tpPointsChoose))
        for i in range(len(tpPointsChoose) - 1):
            print('i', i)
            cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (255, 0, 0), 2)
        cv2.imshow('src', img2)
        # 到達點位上限後儲存點位
        if (pointsCount == pointsMax):
            np.savetxt("line.txt",tpPointsChoose,fmt='%1.4e')
            cv2.destroyAllWindows()# 關閉視窗
        
    # -------------------------右鍵按下清除軌跡-----------------------------
    if event == cv2.EVENT_RBUTTONDOWN:  # 右鍵點擊
        print("right-mouse")
        pointsCount = 0
        tpPointsChoose = []
        print(len(tpPointsChoose))
        for i in range(len(tpPointsChoose) - 1):
            print('i', i)
            cv2.line(img2, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
        cv2.imshow('src', img2)
 
# -----------------------定點ROI繪製，本程式未使用-------------------
def fixed_ROI():
    mask = np.zeros(img.shape, np.uint8)
    pts = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], np.int32)  # 顶点集
    pts = pts.reshape((-1, 1, 2))
    mask = cv2.polylines(mask, [pts], True, (255, 255, 255))
    mask2 = cv2.fillPoly(mask, [pts], (255, 255, 255))
    cv2.imshow('mask', mask2)
    # cv2.imwrite('mask.bmp', mask2)
    # cv2.drawContours(mask,points,-1,(255,255,255),-1)
    ROI = cv2.bitwise_and(mask2, img)
    cv2.imshow('ROI', ROI)

if __name__ == "__main__":
    vedio_path = r"C:\Users\simon\Desktop\track3.7_windows/2.mp4"
    cap = cv2.VideoCapture(vedio_path)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 2);
    cap.set(3, 1920)
    cap.set(4, 1080)
    cv2.namedWindow('src')
    cv2.resizeWindow('src',900,900)
    cv2.setMouseCallback('src', on_mouse)
    ret,frame_read = cap.read()
    img = frame_read
    img = cv2.resize(img,(608,608))
    cv2.imshow('src',img)
    cv2.waitKey(0)


    