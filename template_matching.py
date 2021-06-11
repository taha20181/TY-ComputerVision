import cv2 as cv
import numpy as np

image = cv.imread('human.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
template = cv.imread('eye-template.jpg', 0)

w, h = template.shape[::-1]

res = cv.matchTemplate(gray, template, cv.TM_CCOEFF_NORMED)
print(res)

threshold = 0.9
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv.rectangle(image, pt, (pt[0] + w, pt[1]+h), (255,0,0), 1)

cv.imshow('Image', image)
cv.imshow('Template', template)
cv.waitKey(0)