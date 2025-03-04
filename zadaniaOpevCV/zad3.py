import cv2 as cv


image = cv.imread('maroko.jpg', cv.IMREAD_GRAYSCALE)

if image is None:
    print("Can't load image.")
else:
    c = len(image.shape)
    print(f'channels: {c}')