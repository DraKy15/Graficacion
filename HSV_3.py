import numpy as np
import cv2 as cv

img = cv.imread('C:\\Users\\ameti\\Pictures\\frutas.png')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
kernel = np.ones((5,5),np.uint8)

# ROJO
maskR1 = cv.inRange(hsv, np.array([0, 70, 50]), np.array([10, 255, 255]))
maskR2 = cv.inRange(hsv, np.array([170, 70, 50]), np.array([180, 255, 255]))
mask_roja = maskR1 + maskR2

#  VERDE
mask_verde = cv.inRange(hsv, np.array([35, 40, 40]), np.array([85, 255, 255]))

# AMARILLO
mask_amarilla = cv.inRange(hsv, np.array([20, 100, 100]), np.array([30, 255, 255]))


def limpiar_mascara(mask):
    # Apertura para quitar ruido externo y cierra para huecos internos
    temp = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    return cv.morphologyEx(temp, cv.MORPH_CLOSE, kernel)


m_roja_clean = limpiar_mascara(mask_roja)
m_verde_clean = limpiar_mascara(mask_verde)
m_amarilla_clean = limpiar_mascara(mask_amarilla)

# Análisis de Regiones
def analizar_frutas(nombre_color, mascara):
    # Identificar regiones conectadas
    # num_labels incluye el fondo (label 0)
    num_labels, labels, stats, centroids = cv.connectedComponentsWithStats(mascara, connectivity=8)
    
    umbral_area = 500 
    contador_frutas = 0
    
    print(f"\n--- ANALISIS COLOR: {nombre_color} ---")
    

    for i in range(1, num_labels):
        area = stats[i, cv.CC_STAT_AREA]
        
        if area >= umbral_area:
            contador_frutas += 1
            print(f"Fruta detectada #{contador_frutas} | Área: {area} px")
        # Si el área es menor al umbral, se ignora
            
    print(f"TOTAL DETECTADO ({nombre_color}): {contador_frutas}")
    return contador_frutas

# Ejecuta el análisis para cada máscara
analizar_frutas("ROJO", m_roja_clean)
analizar_frutas("VERDE", m_verde_clean)
analizar_frutas("AMARILLO", m_amarilla_clean)

# Resultados visuales
resR = cv.bitwise_and(img, img, mask=m_roja_clean)
resV = cv.bitwise_and(img, img, mask=m_verde_clean)
resA = cv.bitwise_and(img, img, mask=m_amarilla_clean)

cv.imshow('Rojo Limpio', resR)
cv.imshow('Verde Limpio', resV)
cv.imshow('Amarillo Limpio', resA)

cv.waitKey(0)
cv.destroyAllWindows()
