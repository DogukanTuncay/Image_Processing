# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:26:34 2024

@author: Doğukan
"""

import cv2
import pickle
import numpy as np


width = 27
height = 15
def checkParkSpace(imgg):
    spaceCounter = 0
    for pos in posList:
        x,y = pos
        img_crop = imgg[y: y+height, x: x+width]
        count = cv2.countNonZero(img_crop)
        print("Miktar:",count)
        if count < 150:
            color = (0,255,0)
            spaceCounter +=1
        else:
            color = (0,0,255)
            
        cv2.rectangle(img, pos, (pos[0]+width,pos[1]+height),color,2)
        cv2.putText(img,str(count),(x,y+height-5),cv2.FONT_HERSHEY_PLAIN,1,color,2)
    cv2.putText(img,f"Free:{spaceCounter}/{len(posList)}",(15,24),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),2)
      
        
try:
    with open("CarParkPos","rb") as f:
        posList = pickle.load(f)
except:
    posList = []
    
    
cap = cv2.VideoCapture("datas/video.mp4")

while True:
    success,img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold,5)
    imgDilate = cv2.dilate(imgMedian,np.ones((3,3),np.uint8),iterations=1)
    checkParkSpace(imgDilate)
    
    cv2.imshow("imgBlur",img)
    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(200) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()