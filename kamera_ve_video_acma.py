# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:13:40 2024

@author: Doğukan
"""

#kamera açma ve video kaydı

import cv2

# bşaka bir kamera varsa 0-1-2 gibi denemek gerek.
cap = cv2.VideoCapture(0)


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)


writer = cv2.VideoWriter("video_kaydi.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20, (width,height))

while True:
    ret, frame = cap.read()
    cv2.imshow("Video",frame)
    
    #kaydetme
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):break
    
#bitirme işlemi
cap.release()
writer.release()
cv2.destroyAllWindows()