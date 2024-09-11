# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:55:21 2024

@author: Doğukan
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("datas/odev1.jpg",0)

plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("Başlık")

resized_img = cv2.resize(img, dsize = (int(860*4/5),860))

print(resized_img.shape)

plt.figure(), plt.imshow(resized_img), plt.axis("off"), plt.title("Başlık")

text_img = img.copy()
cv2.putText(text_img, "Kopek", (200, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

plt.figure(), plt.imshow(text_img), plt.axis("off"), plt.title("Kopek yazılı")


ret, thresh = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

plt.figure(), plt.imshow(thresh), plt.axis("off"), plt.title("Threshold")

blur = cv2.GaussianBlur(img,(5,5),0)


plt.figure(), plt.imshow(blur), plt.axis("off"), plt.title("Gaussian")

laplacian = cv2.Laplacian(img,cv2.CV_64F)

plt.figure(), plt.imshow(laplacian), plt.axis("off"), plt.title("Laplacian")

plt.figure()
img = cv2.imread("datas/odev1.jpg", cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img],[0],None,[256],[0,256])

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()