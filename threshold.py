import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("avatar.jpg",cv2.IMREAD_GRAYSCALE)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
thresh6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)
titles = ['BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV', 'ADAPTIVE']
images = [thresh1, thresh2, thresh3, thresh4, thresh5, thresh6]

for i in range(6):
    plt.subplot(3,2,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([1]), plt.yticks([1])
plt.show()