import cv2 as cv
import imutils

image = cv.imread("tajMahal.jpg")
cv.imshow("Original", image)

resized = imutils.resize(image, height=400)
cv.imshow("Resized", resized)


cv.waitKey(0)
cv.destroyAllWindows()