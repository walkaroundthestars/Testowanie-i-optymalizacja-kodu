import cv2 as cv

image = cv.imread('monaco.jpg')

(h, w) = image.shape[:2]
startX = 0
while startX + 100 < w:
    startX += 10
    roi = image[0:h, startX:startX+100]
    cv.imshow("Camera", roi)
    cv.waitKey()

cv.waitKey(0)
cv.destroyAllWindows()