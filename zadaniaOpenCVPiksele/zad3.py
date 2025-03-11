import cv2 as cv

image = cv.imread('fox.jpg')

if image is None:
    print("Can't load image.")
else:
    (h,w,c) = image.shape
    (cX, cY) = (w // 2, h // 2)
    (b, g, r) = image[cX, cY]
    print(f"Red: {r}, Green: {g}, Blue: {b}")
    cv.waitKey(0)
    cv.destroyAllWindows()