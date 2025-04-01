import cv2 as cv

image = cv.imread('monaco.jpg')
cv.imshow("Image", image)

roi = image[0:100, 0:100]
cv.imshow("Left top corner", roi)

cv.waitKey(0)
cv.destroyAllWindows()