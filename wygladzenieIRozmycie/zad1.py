import cv2 as cv

image = cv.imread('bombaj.jpg')
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

#metoda dwustronna najlepiej usuwa szum, bo daje efekt "wygładzenia" zdjęcia z zachowaniem jego elementów
#najwięcej szczegółów również zachowuje metoda dwustronna


#rozmycie proste - utrudnia rozpoznanie obiektów widocznych na zdjęciu.
#rozmycie Gaussa - rozmycie jest równomierne i gładsze niż proste, obiekty są nadal możliwe do rozpoznania.
#rozmycie medianowe - rozmywa obraz zachowując zarys obiektów i kształtów, co może
#pomagać w rozpoznawaniu obiektów, nie zwracając uwagi na szczegóły.
#rozmycie dwustronne - wygładza obraz, pozostawiając widoczne obiekty co może być wadą jak i zaletą.
#Da się dzięki temu uzyskać naturalny efekt, ale nie pomaga jeżeli chcemy utrudnić rozpoznanie danych obiektów.