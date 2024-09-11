# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:47:47 2024

@author: Doğukan
"""

import cv2
import numpy as np
img = cv2.imread("datas/lenna.png")

hor = np.hstack((img,img))

cv2.imshow("Horizontal",hor)
cv2.waitKey(0)
cv2.destroyAllWindows()

#dikey

ver = np.vstack((img,img))
cv2.imshow("dikey",ver)
cv2.waitKey(0)
cv2.destroyAllWindows()




