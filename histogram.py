# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = np.zeros((200,200), np.uint8)

# cv2.rectangle(img, (0,100), (200,200), (255), -1)
# cv2.rectangle(img, (0,50), (100,100), (127), -1)

# cv2.imshow("Image",img)

# plt.hist(img.ravel(),256,[0,256])
# plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Case 2 : Using Color Image:
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("taha.jpg", 1)
# cv2.imshow("Image",img)
b,g,r = cv2.split(img)
# cv2.imshow("blue",b)
# cv2.imshow("Green",g)
# cv2.imshow("Red",r)
plt.hist(img.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# img = cv2.imread("taha.jpg")
# hist = cv2.calcHist([img],[0], None, [256], [0,256])
# plt.plot(hist)
# plt.show()