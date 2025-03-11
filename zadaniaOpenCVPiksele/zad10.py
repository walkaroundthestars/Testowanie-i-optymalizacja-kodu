import cv2 as cv

image = cv.imread('fox.jpg')

if image is None:
    print("Can't load image.")
else:
    (b, g, r) = image[50, 50]
    print(f"Red: {r}, Green: {g}, Blue: {b}")

    (b2, g2, r2) = image[200, 200]
    print(f"Red: {r2}, Green: {g2}, Blue: {b2}")

    print(f"The difference is {abs(r-r2)} in red, {abs(g-g2)} in green and {abs(b-b2)} in blue.")
    cv.waitKey(0)
    cv.destroyAllWindows()