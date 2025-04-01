import cv2 as cv

image = cv.imread('monaco.jpg')

(h, w) = image.shape[:2]
leftLine = w//3
rightLine = 2*w//3
topLine = h//3
bottomLine = 2*h//3

roi1 = image[0:topLine, 0:leftLine]
roi2 = image[0:topLine, leftLine:rightLine]
roi3 = image[0:topLine, rightLine:w]
roi4 = image[topLine:bottomLine, 0:leftLine]
roi5 = image[topLine:bottomLine, leftLine:rightLine]
roi6 = image[topLine:bottomLine, rightLine:w]
roi7 = image[bottomLine:h, 0:leftLine]
roi8 = image[bottomLine:h, leftLine:rightLine]
roi9 = image[bottomLine:h, rightLine:w]

cv.imshow("roi1", roi1)
cv.imshow("roi2", roi2)
cv.imshow("roi3", roi3)
cv.imshow("roi4", roi4)
cv.imshow("roi5", roi5)
cv.imshow("roi6", roi6)
cv.imshow("roi7", roi7)
cv.imshow("roi8", roi8)
cv.imshow("roi9", roi9)

cv.waitKey(0)
cv.destroyAllWindows()