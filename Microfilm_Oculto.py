import cv2
import numpy as np



img = cv2.imread('C:\\Users\\ameti\\Pictures\\microfilm.jpg')



# Recorte sugerido (Ajusta las coordenadas según necesites)

recorte = img[900:1100, 900:1100]

# ==========================================
# MÉTODO 1: MODO RAW (Vecino más cercano manual)
# ==========================================
# 1. Crea un lienzo 5 veces más grande que el recorte

Lienzo = np.zeros((recorte.shape[0]*5, recorte.shape[1]*5, 3), dtype=np.uint8)

# 2. Multiplica las coordenadas para mapear los colores

recorte_Multi = np.repeat(np.repeat(recorte, 5, axis=0), 5, axis=1)


# ==========================================
# MÉTODO 2: MODO OPENCV (Interpolación)
# ==========================================
# 1. Usa cv2.resize con fx=5, fy=5 e interpolation=cv2.INTER_CUBIC

cv2.resize(recorte, (0, 0), fx=5, fy=5, interpolation=cv2.INTER_CUBIC)


cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen_Raw', recorte_Multi)
cv2.imshow('Imagen_Opencv', cv2.resize(recorte, (0, 0), fx=5, fy=5, interpolation=cv2.INTER_CUBIC))
cv2.waitKey(0)