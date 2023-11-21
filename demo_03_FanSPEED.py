import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
dev_port = 0
camera = cv.VideoCapture(dev_port)
if camera.isOpened():
	is_reading, img = camera.read()
	if is_reading:
		plt.imshow(img)
		plt.show()
