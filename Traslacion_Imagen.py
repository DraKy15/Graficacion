import cv2
import numpy as np


# Cargar la imagen
img = cv2.imread('C:\\Users\\ameti\\Pictures\\vehiculo.jpg')


# ==========================================
# MÉTODO 1: MODO RAW (Manipulación de Píxeles)
# ==========================================
# 1. Crea un lienzo negro vacío (np.zeros) de 600x800

lienzo = np.zeros((600, 800, 3), dtype=np.uint8)

alto, ancho = img.shape[:2]


# 2. Mueve los píxeles al nuevo lienzo sumando 300 en X y 200 en Y

for i in range(alto):
    for j in range(ancho):
        # Calculamos la nueva posición
        nueva_y = i + 200
        nueva_x = j + 300
        
        
        if nueva_y < 600 and nueva_x < 800:
            lienzo[nueva_y, nueva_x] = img[i, j]

cv2.imshow('Imagen Trasladada', lienzo)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==========================================
# MÉTODO 2: MODO OPENCV (Matriz de Transformación)
# ==========================================
# 1. Crea la matriz de traslación 'M' en NumPy

Matriz = np.float32([[1, 0, 300], [0, 1, 200]])

# 2. Aplica cv2.warpAffine a la imagen original
img_trasladada = cv2.warpAffine(img, Matriz, (800, 600))

cv2.imshow('Imagen Trasladada (Metodo 2)', img_trasladada)
cv2.waitKey(0)
cv2.destroyAllWindows()