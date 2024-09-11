# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:28:51 2024

@author: Doğukan
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

def gaussianNoise(image):
    """
    Giriş görüntüsüne Gauss gürültüsü ekleyen fonksiyon.
    """
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var ** 0.5  # Sigma, varyansın kareköküdür
    
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    noisy = image + gauss
    
    return noisy

# Görüntüyü yükle
img = cv2.imread("datas/NYC.jpg")

# Görüntüyü RGB formatına dönüştür
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Orijinal görüntüyü göster
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal")
plt.show()

# Ortalama Bulanıklaştırma Yöntemi
dst2 = cv2.blur(img, ksize=(3, 3))
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("Ortalama Bulanıklık")
plt.show()

# Gaussian Blur
gb = cv2.GaussianBlur(img, ksize=(3, 3), sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Gaussian Blur")
plt.show()

# Medyan Blur
mb = cv2.medianBlur(img, ksize=3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("Medyan Blur")
plt.show()

# Gaussian gürültüsü ekle ve sonucu göster
gaussianNoisyImage = gaussianNoise(img)
plt.figure()
plt.imshow(gaussianNoisyImage)
plt.axis("off")
plt.title("Gaussian Noise")
plt.show()


def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    
    # Salt (beyaz) ekleme
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i, int(num_salt)) for i in image.shape[:2]]
    noisy[tuple(coords)] = 1

    # Pepper (siyah) ekleme
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
    coords = [np.random.randint(0, i, int(num_pepper)) for i in image.shape[:2]]
    noisy[tuple(coords)] = 0
    
    return noisy

# Salt and Pepper gürültüsü ekle

spImage = saltPepperNoise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("SP Image")




# Medyan Blur
mb = cv2.medianBlur(spImage, ksize=3)
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("Medyan Blur")
plt.show()


















