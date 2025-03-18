import cv2 as cv
import numpy as np

canvas = np.zeros((400, 400, 3), dtype="uint8")

green = (0, 255, 0)
red = (0, 0, 255)

cv.rectangle(canvas, (0, 0), (100, 50), green)
cv.rectangle(canvas, (300, 350), (400, 400), red, 3)
cv.imshow("Canvas", canvas)
cv.waitKey(0)