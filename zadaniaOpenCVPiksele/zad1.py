import cv2 as cv


image = cv.imread('louvre.jpg')

if image is None:
    print("Can't load image.")
else:
    (b, g, r) = image[0, 0]
    print(f"Red: {r}, Green: {g}, Blue: {b}")
    cv.waitKey(0)
    cv.destroyAllWindows()