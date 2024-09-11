# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:06:53 2024

@author: Doğukan
"""

import cv2
import numpy as np

def region_of_interest(image,vertices):
    mask = np.zeros_like(image)
    match_mask_color = 255
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv2.bitwise_and(image,mask)
    
    return masked_image


def drawLines(image,lines):
    image = np.copy(image)
    blank_image = np.zeros((image.shape[0],image.shape[1],3),dtype=np.uint8)
    
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),thickness = 10)
    image = cv2.addWeighted(image, 0.8, blank_image, 1, 0.0)
    return image

def process(image):
    h,w,_ = img.shape
    
    region_of_interest_vertices = [(0,h),(w/2,h/2),(w,h)]
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  
    
    canny_image = cv2.Canny(gray_image,250,120)
    
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices],np.int32))
    lines = cv2.HoughLinesP(cropped_image, rho = 2, theta = np.pi/180, threshold = 220,lines = np.array([]),minLineLength=150,maxLineGap=5)
    
    imageWithLine = drawLines(image,lines)
    
    return imageWithLine

cap = cv2.VideoCapture("datas/road_line_video2.mp4")

while True:
    success,img = cap.read()
    img = process(img)        
    if success:
        cv2.imshow("img",img)

        # 'q' tuşuna basıldığında döngüyü sonlandır
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
        
    else: break
cap.release()
cv2.destroyAllWindows()