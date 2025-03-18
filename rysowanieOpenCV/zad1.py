import cv2 as cv
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
(h,w,c) = canvas.shape
(cX, cY) = (w // 2, h // 2)

blue = (255, 0, 0)
cv.line(canvas, (cX, cY) , (300, 300), blue, 2)
cv.imshow("Canvas", canvas)
cv.waitKey(0)