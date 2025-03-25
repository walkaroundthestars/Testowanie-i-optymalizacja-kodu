import cv2 as cv
import imutils

image = cv.imread("tajMahal.jpg")
cv.imshow("Original", image)

(h, w) = image.shape[:2]

resized = imutils.resize(image, width=w*3, inter=cv.INTER_NEAREST)
cv.imshow("Resized with nearest", resized)

resized2 = imutils.resize(image, width=w*3, inter=cv.INTER_LINEAR)
cv.imshow("Resized with linear", resized2)

resized3 = imutils.resize(image, width=w*3, inter=cv.INTER_CUBIC)
cv.imshow("Resized with cubic", resized3)

resized4 = imutils.resize(image, width=w*3, inter=cv.INTER_LANCZOS4)
cv.imshow("Resized with lanczos4", resized4)

cv.waitKey(0)
cv.destroyAllWindows()