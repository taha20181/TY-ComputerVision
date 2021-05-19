import cv2 as cv
import imutils as imu

image = cv.imread('Webonise-Lab-Logo.png')

rotated_image = imu.rotate(image, angle=45)
rotated_image_ = imu.rotate(image, angle=90)

cv.imshow("Og", image)
cv.imshow("45", rotated_image)
cv.imshow("90", rotated_image_)

cv.waitKey(0)