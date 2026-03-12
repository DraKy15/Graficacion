# Misiones


### Amet Pérez Acosta 
### N° de Control: 22121293
### Grupo B

----------


# Misión 1

![](../Pictures/vehiculo.jpg)


Código de respuesta:


```python

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
```


**¿Notaste alguna diferencia de tiempo al procesar la imagen píxel por píxel con ciclos for (Modo Raw) en comparación con la función cv2.warpAffine de OpenCV? ¿Por qué crees que tu código manual tarda mucho más en ejecutarse?**

- Pude percibir que, al realizar el procesado de la imagen por medio de los ciclos, terminaba siendo más complicado ya que implica que se debe recorrer de a uno por uno los pixeles, siendo más fácil de optimizar gracias a las funciones predefinidas y la gestión de memoria mejor aprovechado en la función cv2.warpAffine de OpenCV.


![](../Pictures/Screenshots/Traslacion_Imagen 1.jpg)

![](../Pictures/Screenshots/Traslacion_Imagen 2.png)


# Misión 2

![](../Pictures/qr_rotado.jpg)


Código de respuesta:


```python
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

```

**Al calcular la rotación píxel por píxel con tus fórmulas matemáticas (Modo Raw), ¿te quedaron 'puntos negros' o píxeles sin color esparcidos en la imagen resultante? ¿Cómo te imaginas que algoritmos profesionales como los de OpenCV logran rotar la imagen sin dejar esos huecos vacíos?**


No, yo pienso que es por medio de las mismas funciones trignometricas y la manera que en que se rellenan por el mapeo inverso y cierta intensidad que permite hacer un cálculo más exacto.

![](../Pictures/Screenshots/Codigo_Mareado_Raw.png)

![](../Pictures/Screenshots/Codigo_Mareado.png)


# Misión 3

![](../Pictures/microfilm.jpg)

Código de respuesta:

```python

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

```

**Al comparar visualmente el texto ampliado, ¿qué diferencia notas en los bordes de las letras entre tu resultado del Modo Raw y el de OpenCV usando la interpolación cv2.INTERCUBIC? ¿De dónde crees que OpenCV saca los colores para rellenar y suavizar esos píxeles nuevos que en la imagen original no existían?**

Noto una mayor definición en los bordes y mayor resolución en los pixeles de las letras con OpenCV que con Raw, al presentar menos dientes de sierra. Puede ser que sea por las mismas funciones que permiten un suavizado más preciso y consistente de los pixeles gracias a un promedio ponderado de los pixeles alrededor.


![](../Pictures/Screenshots/Microfilm_Raw.png)


![](../Pictures/Screenshots/Microfilm_OpenCV.png)