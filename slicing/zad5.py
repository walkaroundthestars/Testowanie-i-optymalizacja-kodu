import cv2 as cv

image = cv.imread('face.jpg')
cv.imshow("Image", image)

roi = image[50:210, 210:330]
cv.imshow("Face", roi)

cv.waitKey(0)
cv.destroyAllWindows()