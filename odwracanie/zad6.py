import cv2 as cv

image = cv.imread('obraz.jpg')

print("How should I flip the image?")
number = int(input())

if (number == 0 or number == 1 or number == -1):
    flipped = cv.flip(image, number)
    cv.imshow("Flipped horizontally and vertically", flipped)
else:
    print("Wrong value")

cv.waitKey(0)
cv.destroyAllWindows()