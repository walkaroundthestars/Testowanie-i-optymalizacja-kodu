import cv2 as cv


image = cv.imread('maroko.jpg')

if image is None:
    print("Can't load image.")
else:
    c = len(image.shape)
    print(f'channels: {c}')