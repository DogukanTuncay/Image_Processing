import cv2
# içe aktarma
image = cv2.imread('datas/messi5.jpg',0)

#görselleştir

cv2.imshow("Ilk Resim",image)
k = cv2.waitKey(0)

if k  ==27:    
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('datas/mess_gray.png',image)
    cv2.destroyAllWindows()
    
    
