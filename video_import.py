# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:06:36 2024

@author: Doğukan
"""

import cv2
import time


#video path
video_name = "datas/MOT17-04-DPM.mp4"


#videoyu içe aktaralım
cap = cv2.VideoCapture(video_name)
if cap.isOpened == False:
    print("Hata")
    
print("Genişlik:",cap.get(3))
print("Yükseklik:",cap.get(4))

while True:
    ret, frame = cap.read()
    
    if ret == True:
        time.sleep(0.1) # kullanmazsak çok hızlı akar
        
        cv2.imshow("Video",frame)
    else: break

    if cv2.waitKey(1) & 0xFF  == ord("q"):
        break
    
cap.release
cv2.destroyAllWindows()