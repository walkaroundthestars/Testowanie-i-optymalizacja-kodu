import cv2 as cv

image = cv.imread('mountainsWithNoise.png')
cv.imshow("Image", image)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

for diameter, sigmaColor, sigmaSpace in params:
    blurred = cv.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    cv.imshow("Rozmycie dwustronne ({}, {}, {})".format(diameter, sigmaColor, sigmaSpace), blurred)
    cv.waitKey(0)

kX, kY = 9,9
blurred = cv.blur(image, (kX, kY))
cv.imshow("Rozmycie proste", blurred)
cv.waitKey(0)

blurred = cv.GaussianBlur(image, (kX, kY),0)
cv.imshow("Rozmycie Gaussa", blurred)
cv.waitKey(0)

blurred = cv.medianBlur(image, kX)
cv.imshow("Rozmycie medianowe", blurred)
cv.waitKey(0)

cv.destroyAllWindows()

#zmniejsza szum, jednak nie redukuje go całkowicie

#zachowuje krawędzie skutecznie, ale medianowe odrobinę lepiej

#jak największy rozmiar kernela redukuje najskuteczniej szum