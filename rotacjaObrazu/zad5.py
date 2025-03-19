import cv2 as cv
import imutils

image = cv.imread('eiffel.jpg')
cv.imshow("Image", image)


rotated = imutils.rotate(image, 180)
cv.imshow("Rotated by 180 Degrees", rotated)

cv.waitKey(0)
cv.destroyAllWindows()
