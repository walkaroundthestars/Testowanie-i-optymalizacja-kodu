import cv2 as cv

image = cv.imread('obraz.jpg')
cv.imshow('Original', image)

flippedVer = cv.flip(image, 0)
cv.imshow("Flipped vertically", flippedVer)

flippedHor = cv.flip(image, 1)
cv.imshow("Flipped horizontally", flippedHor)

flippedHorAndVer = cv.flip(image, -1)
cv.imshow("Flipped horizontally and vertically", flippedHorAndVer)

cv.waitKey(0)
cv.destroyAllWindows()