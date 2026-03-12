
import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\ameti\\Pictures\\frutas.png')


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# ROJO
maskR1 = cv.inRange(hsv, np.array([0, 70, 50]), np.array([10, 255, 255]))
maskR2 = cv.inRange(hsv, np.array([170, 70, 50]), np.array([180, 255, 255]))
mask_roja = maskR1 + maskR2

# VERDE
mask_verde = cv.inRange(hsv, np.array([35, 40, 40]), np.array([85, 255, 255]))

# AMARILLO
mask_amarilla = cv.inRange(hsv, np.array([20, 100, 100]), np.array([30, 255, 255]))


resR = cv.bitwise_and(img, img, mask=mask_roja)
resV = cv.bitwise_and(img, img, mask=mask_verde)
resA = cv.bitwise_and(img, img, mask=mask_amarilla)


cv.imshow('Rojo', resR)
cv.imshow('Verde', resV)
cv.imshow('Amarillo', resA)
cv.imshow('Original', img)
cv.imshow('Hsv', hsv)

cv.waitKey(0)
cv.destroyAllWindows()