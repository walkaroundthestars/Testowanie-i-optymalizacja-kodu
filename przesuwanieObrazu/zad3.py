import cv2 as cv
import numpy as np

image = cv.imread('paris.jpg')

cv.imshow("Image", image)

M = np.float32([[1, 0, -370], [0, 1, -300]])
shifted = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv.imshow("Shifted up and left", shifted)

cv.waitKey(0)
cv.destroyAllWindows()