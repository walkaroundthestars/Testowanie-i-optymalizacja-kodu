import cv2 as cv
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

red = (0, 0, 255)
blue= (255,0,0)

(h,w,c) = canvas.shape
(cX, cY) = (w // 2, h // 2)

cv.rectangle(canvas, (100,100), (200, 200), blue)
cv.circle(canvas, (cX, cY), 30, red)
cv.imshow("Canvas", canvas)
cv.waitKey(0)