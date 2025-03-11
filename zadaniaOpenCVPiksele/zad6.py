import cv2 as cv

image = cv.imread('fox.jpg')

if image is None:
    print("Can't load image.")
else:
    (h,w,c) = image.shape
    (cX, cY) = (w // 2, h // 2)
    image[cX-50:cX+50, cY-50:cY+50] = (0,0,255)

    cv.imshow('image after change', image)
    cv.waitKey(0)
    cv.destroyAllWindows()