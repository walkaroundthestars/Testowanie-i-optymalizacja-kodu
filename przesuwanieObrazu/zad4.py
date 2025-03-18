import cv2 as cv
import imutils

image = cv.imread('paris.jpg')

cv.imshow("Image", image)

shifted = imutils.translate(image, 100, 50)
cv.imshow("Shifted Down", shifted)

cv.waitKey(0)
cv.destroyAllWindows()