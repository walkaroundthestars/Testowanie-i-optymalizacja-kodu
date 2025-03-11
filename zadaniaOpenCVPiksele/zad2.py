import cv2 as cv


image = cv.imread('fox.jpg')

if image is None:
    print("Can't load image.")
else:
    cv.imshow('image before change', image)

    (h,w,c) = image.shape

    image[h-1,w-1] = (0,0,255)

    cv.imshow('image after change', image)
    cv.waitKey(0)
    cv.destroyAllWindows()