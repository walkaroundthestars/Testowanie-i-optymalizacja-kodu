import cv2 as cv
import imutils

image = cv.imread("tajMahal.jpg")

(h, w) = image.shape[:2]

for i in range(100,320,20):
    resized = imutils.resize(image, width=(w*i)//100)
    cv.imshow("Resized with cubic", resized)
    cv.waitKey(500)

cv.waitKey(0)
cv.destroyAllWindows()