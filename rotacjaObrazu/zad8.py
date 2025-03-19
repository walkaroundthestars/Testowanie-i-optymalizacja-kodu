import cv2 as cv
import imutils

image = cv.imread('eiffel.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
rotated = image
for i in range(1,4):
    M = cv.getRotationMatrix2D((cX, cY), 30, 1.0)
    rotated = cv.warpAffine(rotated, M, (w, h))
cv.imshow("Rotated by 30 x 3", rotated)

rotated2 = imutils.rotate(image, 90)
cv.imshow("Rotated by 90 once", rotated2)

cv.waitKey(0)
cv.destroyAllWindows()
