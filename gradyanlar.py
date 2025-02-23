# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:04:28 2024

@author: Doğukan
"""

import cv2
import matplotlib.pyplot as plt

#resmi içe aktar

img = cv2.imread("datas/sudoku.jpg",0)

plt.figure(), plt.imshow(img,cmap="gray"),plt.axis("off"), plt.title("Orijinal")

#x gradyan

sobelx = cv2.Sobel(img,ddepth=cv2.CV_16S,dx=1,dy=0,ksize=5)


plt.figure(), plt.imshow(sobelx,cmap="gray"),plt.axis("off"), plt.title("Sobelx")

#y gradyan
sobely = cv2.Sobel(img,ddepth=cv2.CV_16S,dx=0,dy=1,ksize=5)

plt.figure(), plt.imshow(sobely,cmap="gray"),plt.axis("off"), plt.title("Sobely")

#laplacian gradyan

laplacian = cv2.Laplacian(img,ddepth=cv2.CV_16S)
plt.figure(), plt.imshow(laplacian,cmap="gray"),plt.axis("off"), plt.title("Laplacian")
