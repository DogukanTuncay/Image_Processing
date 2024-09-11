# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:22:06 2024

@author: Doğukan
"""

import cv2


#resim yolu
image_path = "datas/lenna.png"
img = cv2.imread(image_path,0)
print("resim boyutu :",img.shape)

imgResized = cv2.resize(img,(800,800))

print("Yeniden  boyutlu resim boyutu :",imgResized.shape)

cv2.imshow("Resized :", imgResized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#kırpma

imgCropped = imgResized[:400,:400]
imgCropped2= imgResized[:400,400:800]
imgCropped3 = imgResized[400:800,:400]
imgCropped4 = imgResized[400:800,400:800]


cv2.imshow("Cropped1 :", imgCropped)
cv2.imshow("Cropped2 :", imgCropped2)
cv2.imshow("Cropped3 :", imgCropped3)
cv2.imshow("Cropped4 :", imgCropped4)
cv2.waitKey(0)
cv2.destroyAllWindows()
