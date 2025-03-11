import cv2 as cv

image = cv.imread('fox.jpg')

if image is None:
    print("Can't load image.")
else:
    cv.imshow('image', image)
    (h,w,c) = image.shape
    (cX, cY) = (w // 2, h // 2)
    middlePart = image[int(cX-(w/6)):int(cX+(w/6)), int(cY-(h/6)):int(cY+(h/6))]

    cv.imshow('Middle of image', middlePart)
    cv.waitKey(0)
    cv.destroyAllWindows()