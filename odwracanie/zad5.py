import cv2 as cv

image = cv.imread('obraz.jpg')
cv.imshow('Original', image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

image[0:cY, 0:cX] = cv.flip(image[0:cY, 0:cX], -1)
cv.imshow("Partly flipped", image)
cv.waitKey(0)
cv.destroyAllWindows()