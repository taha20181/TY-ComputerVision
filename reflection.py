import cv2
import matplotlib.pylab as plt
import numpy as np
from numpy.lib.type_check import imag

image = cv2.imread('small.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


plt.axis('off')
plt.imshow(image)
plt.show()

rows, cols, dim = image.shape

M = np.float32(
    [
        [1, 0, 0],
        [0, -1, rows],
        [0, 0, 1]
    ]
)

reflected_image = cv2.warpPerspective(image, M, (int(cols), (int(rows))))
plt.axis('off')
plt.imshow(reflected_image)
plt.show()

plt.imsave('Reflected', reflected_image)