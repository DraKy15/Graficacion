import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\ameti\\Pictures\\frutas.png')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
kernel = np.ones((5,5),np.uint8)

# ROJO
maskR1 = cv.inRange(hsv, np.array([0, 70, 50]), np.array([10, 255, 255]))
maskR2 = cv.inRange(hsv, np.array([170, 70, 50]), np.array([180, 255, 255]))
mask_roja = maskR1 + maskR2

# VERDE
mask_verde = cv.inRange(hsv, np.array([35, 40, 40]), np.array([85, 255, 255]))

# AMARILLO 
mask_amarilla = cv.inRange(hsv, np.array([20, 100, 100]), np.array([30, 255, 255]))

#Por medio de la mascara, pude limpiar la mascara con operaciones morfologicas, para eliminar el ruido y mejorar la deteccion de las frutas
def limpiarmascara(mask,kernel):
    opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)
    closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)
    return closing

mask_roja_limpia = limpiarmascara(mask_roja,kernel)
mask_verde_limpia = limpiarmascara(mask_verde,kernel)
mask_amarilla_limpia = limpiarmascara(mask_amarilla,kernel)


resR = cv.bitwise_and(img, img, mask=mask_roja_limpia)
resV = cv.bitwise_and(img, img, mask=mask_verde_limpia)
resA = cv.bitwise_and(img, img, mask=mask_amarilla_limpia)


cv.imshow('Rojo Limpio', resR)
cv.imshow('Verde Limpio', resV)
cv.imshow('Amarillo Limpio', resA)
cv.imshow('Hsv', hsv)

cv.waitKey(0)
cv.destroyAllWindows()