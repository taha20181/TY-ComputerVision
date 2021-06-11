import cv2 as cv
import imutils as imu

image = cv.imread('Webonise-Lab-Logo.png')

rotated_image = imu.rotate_bound(image, angle=45)
rotated_image_ = imu.rotate_bound(image, angle=90)

cv.imshow("Og", image)
cv.imshow("45", rotated_image)
cv.imshow("90", rotated_image_)

cv.waitKey(0)