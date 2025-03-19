import cv2 as cv

image = cv.imread('eiffel.jpg')
cv.imshow("Image", image)

(h, w) = image.shape[:2]

M = cv.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv.warpAffine(image, M, (w, h))
cv.imshow("Rotated by 30 Degrees", rotated)

cv.waitKey(0)
cv.destroyAllWindows()
