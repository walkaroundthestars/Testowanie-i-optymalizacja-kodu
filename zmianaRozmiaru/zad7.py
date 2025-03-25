import cv2 as cv
import imutils

image = cv.imread("tajMahal.jpg")
cv.imshow("Original", image)

(h, w) = image.shape[:2]

resized = imutils.resize(image, width=w//5, inter=cv.INTER_AREA)
cv.imshow("Resized", resized)


cv.waitKey(0)
cv.destroyAllWindows()