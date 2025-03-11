import cv2 as cv

print("Podaj współrzędną x: ")
x = int(input())
print("Podaj współrzędną y: ")
y = int(input())

image = cv.imread('fox.jpg')

if image is None:
    print("Can't load image.")
else:
    (h,w,c) = image.shape
    if x > h or y > w:
        print("Podane współrzędne wychodzą poza rozmiar zdjęcia")
    else:
        image[x,y] = (0,0,0)

        cv.imshow('image after change', image)
        cv.waitKey(0)
        cv.destroyAllWindows()