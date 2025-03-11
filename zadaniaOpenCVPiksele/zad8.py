import cv2 as cv

image = cv.imread('fox.jpg')

if image is None:
    print("Can't load image.")
else:
    cv.imshow('image', image)
    (h,w,c) = image.shape
    image[100,0:w] = (0, 255, 0)

    cv.imshow('Image after change', image)
    cv.waitKey(0)
    cv.destroyAllWindows()