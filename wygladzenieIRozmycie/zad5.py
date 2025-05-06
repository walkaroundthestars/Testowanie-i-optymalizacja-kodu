import cv2 as cv

#popracować nad szumem

image = cv.imread('bombaj.jpg')
cv.imshow("Image", image)

m = (50,50,50)
s = (50,50,50)
image = cv.randn(image, m, s)
cv.imshow("ImageWithNoise", image)


kX, kY = 9,9
blurred = cv.blur(image, (kX, kY))
cv.imshow("Rozmycie proste", blurred)

blurred = cv.GaussianBlur(image, (kX, kY),0)
cv.imshow("Rozmycie Gaussa", blurred)

blurred = cv.medianBlur(image, kX)
cv.imshow("Rozmycie medianowe", blurred)

diameter = 11
sigmaColor = 61
sigmaSpace = 39

blurred = cv.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
cv.imshow("Rozmycie dwustronne", blurred)
cv.waitKey(0)
cv.destroyAllWindows()