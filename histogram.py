# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:09:51 2024

@author: Doğukan
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi al
# img = cv2.imread("datas/red_blue.jpg")

# img_vis = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.figure(),plt.imshow(img_vis),plt.axis("off"),plt.title("Orijinal")

# print(img.shape)

# img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
# print(img_hist.shape)


# plt.figure(),plt.plot(img_hist)

# color = ("b","g","r")
# plt.figure()
# for i,c in enumerate(color):
#     hist = cv2.calcHist([img], channels=[i], mask=None, histSize=[256], ranges=[0,256])
#     plt.plot(hist,color=c)

#masking

golden_gate = cv2.imread("datas/goldenGate.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)

plt.figure(), plt.imshow(golden_gate_vis)

mask =np.zeros(golden_gate.shape[:2],np.uint8)
plt.figure(), plt.imshow(mask,cmap="gray")

mask[1500:2000,1000:2000] =255

plt.figure(), plt.imshow(mask,cmap="gray")

masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis,mask=mask)

plt.figure(), plt.imshow(masked_img_vis,cmap="gray")

#histogram

masked_img =  cv2.bitwise_and(golden_gate, golden_gate,mask=mask)

masked_img_hist = cv2.calcHist([golden_gate], channels=[0], mask=mask, histSize=[256], ranges=[0,256])

plt.figure(), plt.plot(masked_img_hist)

#histogram eşitleme
#karşıtlık arttırma

img = cv2.imread("datas/hist_equ.jpg",0)
plt.figure(),plt.imshow(img, cmap="gray")

img_hist = cv2.calcHist(img, channels=[0], mask=None, histSize=[256], ranges=[0,256])

plt.figure(), plt.plot(img_hist)

eq_hist = cv2.equalizeHist(img)

plt.figure(), plt.imshow(eq_hist,cmap="gray")


 








