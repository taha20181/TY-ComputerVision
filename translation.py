# import cv2 as cv
# import numpy as np

# image = cv.imread("small.jpg")

# row,col,chan = image.shape

# x = 0
# y = 0

# while(True):
#     trans_matrix = np.float64([[1, 0, x],[0, 1, y]])
#     image1 = cv.warpAffine(image, trans_matrix, (row, col))


#     cv.imshow("frame1", image)
#     cv.imshow("frame2", image1)
#     k = cv.waitKey(3)
#     if k == ord('q'):
#         break
#     x = x + 1
#     y = y + 1


# cv.destroyAllWindows()


import cv2 as cv
import numpy as np

image = cv.imread("small.jpg")

row,col,chan = image.shape

translation_matrix = np.float32(
    [
        [1, 0, 100],
        [0, 1, 200]
    ]
)

# image = cv.rectangle(image, (100, 200), (350, 150), (0, 225, 0), -1)
translated_image = cv.warpAffine(image, translation_matrix, (600, 600))

cv.imshow('Og', image)
cv.imshow('Translated Image', translated_image)


cv.waitKey(0)