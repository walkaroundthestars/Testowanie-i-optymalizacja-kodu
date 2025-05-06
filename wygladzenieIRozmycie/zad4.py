import cv2 as cv

image = cv.imread('harryPotterNewspaper.jpg')
cv.imshow("Image", image)

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

#najmocniej rozmazyją tekst rozmycie medianowe i rozmycie proste

#zachować czytelność pozwala rozmycie dwustronne