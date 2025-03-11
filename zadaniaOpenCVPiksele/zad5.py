import cv2 as cv

image = cv.imread('fox.jpg')

if image is None:
    print("Can't load image.")
else:
    (h,w,c) = image.shape
    (cX, cY) = (w // 2, h // 2)
    image[0:cX,0:cY] = (255,0,0)

    cv.imshow('image after change', image)
    cv.waitKey(0)
    cv.destroyAllWindows()