# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:20:44 2024

@author: Doğukan
"""
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)

mpHand = mp.solutions.hands
hands = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils

tipIds = [4,8,12,16,20]


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    
    lmList = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms,mpHand.HAND_CONNECTIONS)
    
            for id,lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id,cx,cy])
                #işaret uç = 8
                
    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1] :
            fingers.append(1)
        else:
            fingers.append(0)
            

        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] -2 ][2] :
                fingers.append(1)
            else:
                fingers.append(0)
        
        totalF = fingers.count(1)
        print(totalF)
        cv2.putText(img,
                    "Parmak Sayisi :"+str(totalF),
                    (30,125),
                    cv2.FONT_HERSHEY_PLAIN,
                    3,
                    (255,0,0))
    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF  == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()

    
    
    
    
    