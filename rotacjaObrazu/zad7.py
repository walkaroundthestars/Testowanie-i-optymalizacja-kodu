import cv2 as cv
import imutils

image = cv.imread('eiffel.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated1 = cv.warpAffine(image, M, (w, h))
cv.imshow("Rotated with warpAffine", rotated1)

rotated2 = imutils.rotate(image, 60)
cv.imshow("Rotated with imutils", rotated2)

cv.waitKey(0)
cv.destroyAllWindows()
