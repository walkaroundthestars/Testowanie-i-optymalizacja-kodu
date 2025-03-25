import cv2 as cv

image = cv.imread("tajMahal.jpg")
cv.imshow("Original", image)

resized = cv.resize(image, (200,300))
cv.imshow("Resized", resized)


cv.waitKey(0)
cv.destroyAllWindows()