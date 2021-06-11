import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('small.jpg')
rows, cols, ch = image.shape

pt1 = np.float32(
    [
        [50, 100], 
        [200, 50], 
        [50, 200]
    ]
)
pt2 = np.float32(
    [
        [10, 100], 
        [200, 50], 
        [100, 250]
    ]
)

# print(pt1, pt2)

retval=cv2.getAffineTransform(pt1, pt2)
print(retval)
dst=cv2.warpAffine(image, retval, (1000, 1000))
# print(dst)

# cv2.imshow("I/p", image)
# cv2.imshow("O/p", dst)
plt.imshow(dst, 'gray')
plt.show()
cv2.waitKey(0)