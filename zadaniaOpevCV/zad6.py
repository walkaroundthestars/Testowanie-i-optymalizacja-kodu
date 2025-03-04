import cv2 as cv


image = cv.imread('maroko.jpg')

if image is None:
    print("Can't load image.")
else:
    cv.namedWindow('image', cv.WINDOW_NORMAL)
    cv.resizeWindow('image', 800, 600)
    cv.imshow('image', image, )
    cv.waitKey(0)
    cv.destroyAllWindows()