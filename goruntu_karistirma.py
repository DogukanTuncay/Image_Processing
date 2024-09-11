# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:58:40 2024

@author: Doğukan
"""

import cv2
import matplotlib.pyplot as plt

#karıştırma

img1 = cv2.imread("datas/img1.jpg")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.imread("datas/img2.jpg")
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# boyutları farklı, yeniden düzenleyelim eşitleyelim

img1 = cv2.resize(img1,(600,600))
img2 = cv2.resize(img2,(600,600))


print(img1.shape)
print(img2.shape)


plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)


#karıştırma - alpha*img1 + beta*img2

blended = cv2.addWeighted(src1 = img1,alpha=0.4,src2=img2,beta=0.6,gamma=0.5)

plt.figure()
plt.imshow(blended)



















