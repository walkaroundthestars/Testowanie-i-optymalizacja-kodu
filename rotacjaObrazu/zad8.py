import cv2 as cv
import argparse
import imutils

image = cv.imread('eiffel.jpg')
cv.imshow("Image", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
for i in range(1,4):
    M = cv.getRotationMatrix2D((cX, cY), 30, 1.0)
    rotated = cv.warpAffine(image, M, (w, h))
cv.imshow("Rotated by 30 x 3", rotated)

cv.waitKey(0)
cv.destroyAllWindows()
