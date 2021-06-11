import cv2 as cv
import numpy as np

image = cv.imread("small.jpg")

image1 = cv.resize(image, None, fx=1, fy=1.5, interpolation=cv.INTER_LINEAR) # expand
cv.imshow("Linear", image1)

# dsize => desired size for the output image
# fx => scale factor along the horizontal axis
# fy => scale factor along the vertical axis


# cv.imshow("OG", image)
cv.waitKey()
cv.destroyAllWindows()