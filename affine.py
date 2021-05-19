import cv2
import numpy as np


image = cv2.imread('small.jpg')
rows, cols, ch = image.shape

pt1 = np.float32(
    [
        [50, 50], 
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

retval=cv2.getAffineTransform(pt1, pt2)
dst=cv2.warpAffine(image, retval, (600, 600))

cv2.imshow("I/p", image)
cv2.imshow("O/p", dst)

cv2.waitKey(0)