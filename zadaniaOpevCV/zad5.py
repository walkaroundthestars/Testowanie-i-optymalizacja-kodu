import cv2 as cv


image = cv.imread('maroko.jpg')
image2 = cv.imread('houses.jpg')

if image is None or image2 is None:
    print("Can't load image.")
else:
    cv.imshow('image', image)
    cv.imshow('image2', image2)
    cv.waitKey(0)
    cv.destroyAllWindows()