import cv2 as cv

image = cv.imread('obraz.jpg')
cv.imshow('Original', image)

flipped = cv.flip(image, 1)
cv.imshow("Flipped horizontally", flipped)

cv.waitKey(0)
cv.destroyAllWindows()