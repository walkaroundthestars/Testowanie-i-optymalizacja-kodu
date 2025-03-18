import cv2 as cv
import numpy as np

canvas = cv.imread('pawel.jpg')

blue= (255,0,0)
red = (0, 0, 255)
green = (0, 255, 0)

(h,w,c) = canvas.shape
(cX, cY) = (w // 2, h // 2)

cv.circle(canvas, (145, 160), 20, red, -1)
cv.circle(canvas, (210, 150), 20, red, -1)
cv.rectangle(canvas, (140,220), (230, 240), green, -1)
cv.circle(canvas, (175, 170), 100, blue)

cv.imshow("Canvas", canvas)
cv.waitKey(0)