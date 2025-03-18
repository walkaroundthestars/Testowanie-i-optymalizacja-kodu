import cv2 as cv
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")

blue= (255,0,0)

(h,w,c) = canvas.shape
(cX, cY) = (w // 2, h // 2)

for r in range(0, 175, 20):
    cv.rectangle(canvas, (cX-r,cY+r), (cX+r, cY-r), blue)

cv.imshow("Canvas", canvas)
cv.waitKey(0)