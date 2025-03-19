import cv2 as cv
import imutils

image = cv.imread('eiffel.jpg')
cv.imshow("Image", image)

rotated = imutils.rotate_bound(image, -33)
cv.imshow("Rotated by 30 Degrees", rotated)

cv.waitKey(0)
cv.destroyAllWindows()
