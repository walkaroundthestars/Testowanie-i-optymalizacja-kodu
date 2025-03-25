import cv2 as cv
import imutils

image = cv.imread("tajMahal.jpg")
cv.imshow("Original", image)

(h, w) = image.shape[:2]

resized = imutils.resize(image, width=w*3, height=h*3, inter=cv.INTER_LINEAR)
cv.imshow("Resized", resized)


cv.waitKey(0)
cv.destroyAllWindows()