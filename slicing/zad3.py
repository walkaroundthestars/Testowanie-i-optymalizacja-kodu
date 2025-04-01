import cv2 as cv

image = cv.imread('monaco.jpg')
cv.imshow("Image", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

roiRight = image[0:h, cX:w]
cv.imshow("Right half", roiRight)

cv.waitKey(0)
cv.destroyAllWindows()