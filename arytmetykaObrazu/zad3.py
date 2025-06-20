import cv2 as cv
import numpy as np

image = cv.imread('lizbona.jpeg')
cv.imshow("Image", image)

M = np.ones(image.shape, dtype="uint8") * 80
substractNP = cv.subtract(image, M)
cv.imshow("LighterNP", substractNP)

substractCV = cv.subtract(image, 80)
cv.imshow("LighterCV", substractCV)

cv.waitKey(0)
cv.destroyAllWindows()