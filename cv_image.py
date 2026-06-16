import numpy as np
import cv2

img = cv2.imread("input_yoshi.jpeg")

cv2.namedWindow("image", cv2.WINDOW_NORMAL)

print(img.shape)

cv2.imshow("image", img)

while (cv2.waitKey(1)!=97):
    pass


cv2.imwrite("output.png", img)

cv2.destroyAllWindows()