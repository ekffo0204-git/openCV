import numpy as np
import cv2

img = cv2.imread("input_yoshi.jpeg")

cropped = img[50:450, 100:400]

resized = cv2.resize(cropped, (300,300))

cv2.imshow("Original", img)
cv2.imshow("Cropped image", cropped)
cv2.imshow("Resized image", resized)

w, h, c = img.shape
print(f"w={w}")
cv2.waitKey(0)
cv2.destroyAllWindows