import cv2 as cv
import imutils

image = cv.imread("tajMahal.jpg")
cv.imshow("Original", image)

(h, w) = image.shape[:2]

resized = imutils.resize(image, width=800)
cv.imshow("Resized", resized)
cv.imwrite("resized_output.jpg", resized)

cv.waitKey(0)
cv.destroyAllWindows()