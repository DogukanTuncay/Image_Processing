# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:37:47 2024

@author: Doğukan
"""

import cv2
import numpy as np

# ♥ resim oluştur

img = np.zeros((512,512,3),np.uint8) # siyah resim




# çizgi
 # resim, başlangıç noktası, bitiş noktası

cv2.line(img,(100,100),(100,300),(0,255,0))

cv2.imshow("Cizgi",img)

cv2.waitKey(0)

cv2.destroyAllWindows()

#dikdörtgen

cv2.rectangle(img,(100,100),(200,200),(128,128,128),cv2.FILLED)


cv2.imshow("Dikdortgen",img)

cv2.waitKey(0)

cv2.destroyAllWindows()


#daire
# resim, başlangıç, çap, renk


cv2.circle(img,(250,250),30,(128,128,128))


cv2.imshow("cember",img)

cv2.waitKey(0)

cv2.destroyAllWindows()


#metin
# resim, başlangıç noktası, font , kalınlığı, renk

cv2.putText(img,"Resim",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("Metin",img)

cv2.imshow("Metin",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
