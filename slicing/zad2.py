import cv2 as cv

image = cv.imread('monaco.jpg')
cv.imshow("Image", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

roiTop = image[0:cY, 0:w]
roiBottom = image[cY:w, 0:w]
cv.imshow("Bottom half", roiBottom)

cv.waitKey(0)
cv.destroyAllWindows()