import cv2 as cv

image = cv.imread('monaco.jpg')

roi = image[300:400, 300:400]
image[30:130, 30:130] = roi
cv.imshow("Copy, paste", image)

cv.waitKey(0)
cv.destroyAllWindows()