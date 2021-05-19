# Motion Estimation

import cv2 as cv

cap = cv.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()


while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _, thres = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thres, None, iterations=3)
    contour, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    print('Number of contours: ', str(len(contour)))

    cv.drawContours(frame1, contour, -1, (255, 0, 0), 2)

    for cont in contour:

        (x, y, w, h) = cv.boundingRect(cont)

        if cv.contourArea(cont) < 900:
            continue

        cv.rectangle(frame1, (x, y),  (x+w, y+h), (255, 0, 0), 2)
        cv.putText(frame1, "Status : {}".format("Movement"), (10, 20), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv.imshow("Input", frame1)

    frame1 = frame2

    ret, frame2 = cap.read()

    cv.waitKey(0)


cv.destroyAllWindows()
cap.release()