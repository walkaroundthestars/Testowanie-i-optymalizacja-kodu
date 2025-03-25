import cv2 as cv
import imutils

image = cv.imread("tajMahal.jpg")
cv.imshow("Original", image)

(h, w) = image.shape[:2]

resized = imutils.resize(image, width=w*4, inter=cv.INTER_CUBIC)
cv.imshow("Resized with cubic", resized)

resized2 = imutils.resize(image, width=w*4, inter=cv.INTER_LANCZOS4)
cv.imshow("Resized with lanczos4", resized2)

cv.waitKey(0)
cv.destroyAllWindows()