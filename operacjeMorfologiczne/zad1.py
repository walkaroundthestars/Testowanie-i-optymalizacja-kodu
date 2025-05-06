import cv2 as cv
import numpy as np

image = cv.imread('binaryFlower.png')
cv.imshow("Image", image)

eroded = cv.erode(image.copy(), None, iterations=1)
cv.imshow("Eroded {} times".format(1), eroded)
cv.waitKey(0)

cv.destroyAllWindows()

