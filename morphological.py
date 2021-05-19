import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Webonise-Lab-Logo.png", cv2.IMREAD_GRAYSCALE)
x, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

print(mask, x)

kernel = np.ones((3, 3), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=1)
erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
titles = ['image', 'mask', 'dilation', 'erosion',
          'opening', 'closing', 'Morph_Gradient', "Top-HAT"]
images = [img, mask, dilation, erosion, opening, closing, mg, th]
for i in range(8):
    plt.subplot(2, 4, i+1),
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([1]), plt.yticks([1])
plt.show()
