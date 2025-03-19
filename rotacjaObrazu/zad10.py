import cv2 as cv

image = cv.imread('eiffel.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
rotated = image

for i in range(0,24):
    M = cv.getRotationMatrix2D((cX, cY), 15, 1.0)
    rotated = cv.warpAffine(rotated, M, (w, h))
    cv.imshow("Rotation 360", rotated)
    cv.waitKey(500)

cv.waitKey(0)
cv.destroyAllWindows()
