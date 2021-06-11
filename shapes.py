import numpy as np
import cv2

black_image = np.zeros((512,512,3), np.uint8)

cv2.line(black_image,(10,10), (100,100), (255,0,0), 3)

cv2.arrowedLine(black_image, (20,20), (255,255), (255,0,255), 5)

cv2.rectangle(black_image, (50, 100), (200, 40), (255,255,0), 5)

cv2.circle(black_image, (280,200), 100, (255,0,255), -1)

cv2.putText(black_image, "Taha", (280, 200), cv2.FONT_HERSHEY_PLAIN, 5, (255,255,0), 5)

pts = np.array([[25, 70], [25, 160],[110, 200], [200, 160],[200, 70], [110, 20]],np.int32) 
pts = pts.reshape((-1, 1, 2)) 

cv2.polylines(black_image,[pts], False, (255,0,255), 4)

cv2.imshow("black", black_image)
cv2.waitKey(0)
# cv2.destroyAllWindows()