import cv2
import numpy as np


image = cv2.imread('small.jpg')
rows, cols, ch = image.shape

pt1 = np.float32(
    [
        [0, 60], 
        [140, 60], 
        [0, 200],
        [140, 200]
    ]
)
pt2 = np.float32(
    [
        [0, 0], 
        [200, 0],
        [0, 140],
        [200, 140]
    ]
)

retval=cv2.getPerspectiveTransform(pt1, pt2)
dst=cv2.warpPerspective(image, retval, (rows, cols))

cv2.imshow("I/p", image)
cv2.imshow("O/p", dst)

cv2.waitKey(0)

cv2.destroyAllWindows()