import cv2 as cv

image = cv.imread('monaco.jpg')


roi = image[200:500, 200:500]
cv.imwrite("cropped_image.jpg", roi)

cv.waitKey(0)
cv.destroyAllWindows()