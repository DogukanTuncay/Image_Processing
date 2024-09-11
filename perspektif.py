# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:52:21 2024

@author: Doğukan
"""

import cv2
import numpy as np

img = cv2.imread("datas/kart.png")

cv2.imshow(" ",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

width = 400
height = 500

pts1 = np.float32([[203,1],[1,472],
                   [540,150],[338,617]])

pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])


matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("Sonuç :",imgOutput)

cv2.waitKey(0)
cv2.destroyAllWindows()
