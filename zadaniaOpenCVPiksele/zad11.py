import cv2 as cv

image = cv.imread('louvre.jpg')

if image is None:
    print("Can't load image.")
else:
    theBrightest = image[0,0]

    for pixel in image:
        if pixel.any() > theBrightest.any():
            theBrightest = pixel

    print(theBrightest)
    cv.waitKey(0)
    cv.destroyAllWindows()