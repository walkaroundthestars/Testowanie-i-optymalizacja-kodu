import cv2 as cv

image = cv.imread('louvre.jpg')

if image is None:
    print("Can't load image.")
else:
    cv.imshow('image', image)
    image[50:100,50:100] = (255, 255, 255)

    cv.imshow('Image after change', image)
    cv.waitKey(0)
    cv.destroyAllWindows()