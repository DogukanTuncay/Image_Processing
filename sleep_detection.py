# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:30:31 2024

@author: Doğukan
"""

import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

cap = cv2.VideoCapture("datas/sleep_detection_video1.mp4")
detector = FaceMeshDetector()
plotY = LivePlot(540,360,[10,60])
idList = [22,23,24,26,110,157,158,159,160,161,130,243]
color = (0,0,255)
ratioList = []
counter = 0
blickCounter = 0

while True:
    success,img = cap.read()
 
    if success:
        
        img,faces = detector.findFaceMesh(img)
        if faces:
            face = faces[0]
            for id in idList:
                cv2.circle(img,face[id],5,color,cv2.FILLED)
            
            leftUp = face[159]
            leftDown = face[23]
            leftLeft = face[130]
            leftRight = face[243]
            
            lengthVer,_ = detector.findDistance(leftUp, leftDown)
            lengthHor,_ = detector.findDistance(leftLeft, leftRight)
            
            cv2.line(img,leftUp,leftDown,(0,255,0),3)
            cv2.line(img,leftLeft,leftRight,(0,255,255),3)
            ratio = int((lengthVer/lengthHor)*100)
            ratioList.append(ratio)
            if len(ratioList) > 3:
                ratioList.pop(0)
            
            ratioAvg = sum(ratioList)/len(ratioList)
            
            if ratioAvg < 39 and counter == 0:
                blickCounter+=1
                color = (0,255,0)
                counter +=1
            if counter != 0:
                counter +=1
                if counter > 10:
                    counter = 0
                    color = (0,0,255)
            cvzone.putTextRect(img, f"Blink Count : {blickCounter}",(50,100),colorR=color )
            imgPlot = plotY.update(ratioAvg,color)
            img = cv2.resize(img, (640,360))
            imgStack = cvzone.stackImages([img,imgPlot], 2,1)
        
        cv2.imshow("img",imgStack)

        # 'q' tuşuna basıldığında döngüyü sonlandır
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
        
    else: break
cap.release()
cv2.destroyAllWindows()

