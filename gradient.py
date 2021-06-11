import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("human.jpg", cv2.IMREAD_GRAYSCALE)

#Gradient Calculation

# cv2.Laplacian(img, ddepth=6, dst=5, ksize=, scale=, delta=)
lap1 = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
print(lap1)
lap1 = np.uint8(np.absolute(lap1))
print(lap1)
sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelCombine = cv2.bitwise_or(sobelX,sobelY)
titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombine']
images = [img,lap1,sobelX,sobelY,sobelCombine]

for i in range(5):
    plt.subplot(3,2,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([1]), plt.yticks([1])
plt.show()