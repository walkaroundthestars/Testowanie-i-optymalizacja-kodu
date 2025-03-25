import cv2 as cv

image = cv.imread('obraz.jpg')
cv.imshow('Original', image)

flipped = cv.flip(image, 0)
cv.imshow("Flipped vertically", flipped)

cv.waitKey(0)
cv.destroyAllWindows()