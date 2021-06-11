import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)


while True:
    ret, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_l = np.array([110, 50, 50])
    u_l = np.array([150, 255, 255])

    # mask = cv.inRange(hsv, l_l, u_l)

    # res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('Og', frame)
    # cv.imshow('mask', mask)
    # cv.imshow('result', res)


cv.waitKey(0)
cv.destroyAllWindows()