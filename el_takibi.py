# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:22:31 2024

@author: Doğukan
"""

import cv2
import time
import mediapipe as mp
import os
base_options = mp.tasks.BaseOptions(model_asset_path='gesture_recognizer.task',
delegate=mp.tasks.BaseOptions.Delegate.GPU)
os.environ["XDG_CACHE_HOME"] = "C:/python_media"
cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands

hands = mpHand.Hands(max_num_hands = 5)

mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0

while True:
    success,img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms,mpHand.HAND_CONNECTIONS)
            
            for id,lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                
                if id == 4:
                    cv2.circle(img,(cx,cy),9,(255,0,0),cv2.FILLED)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, "FPS"+str(int(fps)),(10,55), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0))
    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF  == ord("q"):
        break
    
cap.release
cv2.destroyAllWindows()

