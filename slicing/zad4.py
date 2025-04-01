import cv2 as cv

image = cv.imread('monaco.jpg')

startX = int(input("Podaj wartość startX: "))
endX = int(input("Podaj wartość endX: "))
startY = int(input("Podaj wartość startY: "))
endY = int(input("Podaj wartość endY: "))

if (startX < endX and startY < endY and startX >= 0 and startY >= 0 and endX >= 0 and endY >= 0):
    roi = image[startY:endY, startX:endX]
    cv.imshow("Sliced image", roi)

cv.waitKey(0)
cv.destroyAllWindows()