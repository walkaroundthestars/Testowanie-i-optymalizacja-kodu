import cv2 as cv

image = cv.imread('bombaj.jpg')
cv.imshow("Image", image)

kernelSizes = [(3, 3), (9, 9), (15, 15)]

for kX, kY in kernelSizes:
    blurred = cv.blur(image, (kX, kY))
    cv.imshow("Rozmycie proste ({}, {})".format(kX, kY), blurred)
    cv.waitKey(0)

for kX, kY in kernelSizes:
    blurred = cv.GaussianBlur(image, (kX, kY),0)
    cv.imshow("Rozmycie Gaussa ({}, {})".format(kX, kY), blurred)
    cv.waitKey(0)

for k in (3, 9, 15):
    blurred = cv.medianBlur(image, k)
    cv.imshow("Rozmycie medianowe ({})".format(k), blurred)
    cv.waitKey(0)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for diameter, sigmaColor, sigmaSpace in params:
    blurred = cv.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    cv.imshow("Rozmycie dwustronne ({}, {}, {})".format(diameter, sigmaColor, sigmaSpace), blurred)
    cv.waitKey(0)
cv.destroyAllWindows()

#czym większy kernel tym efekt jest intensywniejszy
#jak najmniejszy, czyli 3x3
