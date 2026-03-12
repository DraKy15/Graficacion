import cv2
import numpy as np


# Cargar la imagen
img = cv2.imread('C:\\Users\\ameti\\Pictures\\qr_rotado.jpg')

# ==========================================
# MÉTODO 1: MODO RAW (Trigonometría)
# ==========================================
# 1. Crea un lienzo vacío de 500x500

Lienzo=np.zeros((500, 500, 3), dtype=np.uint8)


# 2. Usa las fórmulas de senos y cosenos para mapear los píxeles (¡Cuidado con los huecos negros si mapeas hacia adelante!)
angle=-45

Sen=np.sin(np.radians(angle))
Cos=np.cos(np.radians(angle))

for i in range(500):
    for j in range(500):      
        x_new = i - 250
        y_new = j - 250


# ==========================================
# MÉTODO 2: MODO OPENCV
# ==========================================
# 1. Obtén la matriz con cv2.getRotationMatrix2D


x, y = img.shape[:2]

center = (y // 2, x // 2)

M = cv2.getRotationMatrix2D(center, angle, 1.0)

# 2. Aplica cv2.warpAffine
rotated_img = cv2.warpAffine(img, M, (y, x))

# Mostrar la imagen original y las imagenes rotadas
cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen Rotada', rotated_img)
cv2.imshow('Imagen Rotada_Raw', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



