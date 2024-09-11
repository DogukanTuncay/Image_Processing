# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:06:42 2024

@author: Doğukan
"""

import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("datas/esikleme_img1.JPG")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1, cmap="gray")
plt.axis("off")
plt.show()

# Gri tonlamaya çevirme
gray_img = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)

# Eşikleme
_, threshold_img = cv2.threshold(gray_img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(threshold_img, cmap="gray")
plt.axis("off")
plt.show()

# Uyarlamalı eşik değeri
thresh_img2 = cv2.adaptiveThreshold(gray_img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11, C=8)

plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.show()
