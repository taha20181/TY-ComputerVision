import cv2 as cv
import numpy as np

image = cv.imread("avatar.jpg")

image1 = cv.resize(image, None, fx=1, fy=1.5, interpolation=cv.INTER_LINEAR) # expand
cv.imshow("Linear", image1)

# dsize => desired size for the output image
# fx => scale factor along the horizontal axis
# fy => scale factor along the vertical axis

# image1 = cv.resize(image, fx=1, fy=1.5, interpolation=cv.INTER_AREA) # shrink
# cv.imshow("AREA", image1)

# image1 = cv.resize(image, None, fx=1, fy=1.5, interpolation=cv.INTER_NEAREST)
# cv.imshow("Nearest", image1)

# image1 = cv.resize(image, None, fx=1, fy=1.5, interpolation=cv.INTER_CUBIC)
# cv.imshow("Cubic", image1)

# image1 = cv.resize(image, None, fx=1, fy=1.5, interpolation=cv.INTER_LANCZOS4)
# cv.imshow("Lanczos4", image1)

# image1 = cv.pyrUp(image)
# cv.imshow("pyramid", image1)



cv.imshow("OG", image)
cv.waitKey()
cv.destroyAllWindows()