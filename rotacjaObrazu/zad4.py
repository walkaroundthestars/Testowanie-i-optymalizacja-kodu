import cv2 as cv

print("Podaj kąt o jaki ma być obrócony obraz: ")
x = float(input())

image = cv.imread('eiffel.jpg')
cv.imshow("Image", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv.getRotationMatrix2D((cX, cY), x, 1.0)
rotated = cv.warpAffine(image, M, (w, h))
cv.imshow(f"Rotated by {x} Degrees", rotated)

cv.waitKey(0)
cv.destroyAllWindows()
