# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:40:58 2024

@author: Doğukan
"""

import cv2
import mediapipe as mp
import time

mpFaceDetection = mp.solutions.face_detection
FaceDetection = mpFaceDetection.FaceDetection(0,3)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture("datas/face_detect_video3.mp4")
cTime = 0
pTime = 0
while True:
    success,img = cap.read() 
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
   
    results = FaceDetection.process(imgRGB)
   
    if results.detections:
        for id,detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            h,w,_ = img.shape
            bbox = int(bboxC.xmin*w), int(bboxC.ymin*h),int(bboxC.width*w),int(bboxC.height*h)
            cv2.rectangle(img,bbox,(0,255,255))
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,"FPS:"+str(int(fps)),(10,65),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0))
        
    cv2.imshow("img",img)
    if cv2.waitKey(10) & 0xFF  == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
