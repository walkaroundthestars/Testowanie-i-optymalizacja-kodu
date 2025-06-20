import cv2 as cv
import numpy as np

image = cv.imread('lizbona.jpeg')
cv.imshow("Image", image)

M = np.ones(image.shape, dtype="uint8") * 150
addedNP = cv.add(image, M)
cv.imshow("LighterNP", addedNP)

addedCV = cv.add(image, 150)
cv.imshow("LighterCV", addedCV)

cv.waitKey(0)
cv.destroyAllWindows()