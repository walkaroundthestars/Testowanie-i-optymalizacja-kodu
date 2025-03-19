import cv2 as cv
import imutils

image = cv.imread('eiffel.jpg')

rotated = imutils.rotate(image, 75)
cv.imwrite('eiffelRotated.jpg', rotated)
cv.imshow("Rotated with imutils", rotated)

cv.waitKey(0)
cv.destroyAllWindows()
