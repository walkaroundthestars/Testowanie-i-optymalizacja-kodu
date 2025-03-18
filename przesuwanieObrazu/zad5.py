import cv2 as cv
import imutils

print("Podaj x: ")
x = input()
print("Podaj y: ")
y = input()

image = cv.imread('paris.jpg')

cv.imshow("Image", image)

shifted = imutils.translate(image, x, y)
cv.imshow("Shifted Down", shifted)

cv.waitKey(0)
cv.destroyAllWindows()