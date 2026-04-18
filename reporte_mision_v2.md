# Reporte de Misión: Graficación Táctica II
**Agente Especial:** Amet Pérez Acosta\22121293

---
## Evidencias
### Misión 1
- Imagen recuperada x50:

![](../Pictures/Screenshots/m1_recuperado_x50.png)


- Imagen recuperada x50 + 20:

![](../Pictures/Screenshots/m1_recuperado_x50_mas20.png)


- Código:

```python

img = cv.imread('C:\\Users\\ameti\\Pictures\\m1_oscura 1.png', cv.IMREAD_GRAYSCALE)

#MODO RAW:
# - Crear una matriz int32 para evitar overflow
Matriz = np.float32([[1, 0, 300], [0, 1, 200]])

# - Recorrer con ciclos anidados (y,x) y Multiplicar cada píxel por 50
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i, j] = img[i, j] * 50

# - Aplicar np.clip a 0..255 y guardar como uint8 -> m1_recuperado_x50.png
np.clip(img, 0, 255, out=img)
cv.imwrite('C:\\Users\\ameti\\Pictures\\m1_recuperado_x50.png', img.astype(np.uint8))

# - Sumar +20 a cada píxel recuperado
img_mas20 = np.zeros_like(img, dtype=np.int32)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_mas20[i, j] = img[i, j] + 20    

# - Aplicar np.clip 0..255 y guardar -> m1_recuperado_x50_mas20.png
np.clip(img_mas20, 0, 255, out=img_mas20)
cv.imwrite('C:\\Users\\ameti\\Pictures\\m1_recuperado_x50_mas20.png', img_mas20.astype(np.uint8))   


cv.imshow('Imagen Raw x50 y +20', img_mas20.astype(np.uint8))
cv.imshow('Imagen Raw',img)
cv.waitKey(0) 
cv.destroyAllWindows()


```

### Misión 2
- QR reconstruido: 

![](../Pictures/Screenshots/m2_qr_reconstruido.png)



- Código:

```python
lienzo=np.zeros((400, 400, 3), dtype=np.uint8)

mitad1 = cv.imread('C:\\Users\\ameti\\Pictures\\m2_mitad1.png')
mitad2 = cv.imread('C:\\Users\\ameti\\Pictures\\m2_mitad2.png')


#La mitad 1 debe ser trasladada al origen (0,0).
cv.warpAffine(mitad1, cv.getRotationMatrix2D((0, 0), 0, 1.0), (400, 400), dst=lienzo, borderMode=cv.BORDER_TRANSPARENT)

#La mitad 2 debe ser rotada 180 grados sobre su propio centro y colocada en la parte inferior del lienzo.
np.angle=180
cv.warpAffine(mitad2, cv.getRotationMatrix2D((mitad2.shape[1]//2, mitad2.shape[0]//2), np.angle, 1.0), (400, 400), dst=lienzo, borderMode=cv.BORDER_TRANSPARENT)

#Unir las dos mitades en el lienzo final para revelar el código QR completo
codigo_qr = lienzo
cv.imshow('Codigo QR Unido', codigo_qr)
cv.waitKey(0)
cv.destroyAllWindows()


```



### Misión 3
- Sello forjado:

![](../Pictures/Screenshots/m3_sello_forjado_v2.png)


- Código:

````
img = np.zeros((600, 600, 3), dtype=np.uint8)
img[:] = (40, 20, 20)

# - Dibujar círculo exterior amarillo
circulo_exterior = (300, 300)
radio_exterior = 200
cv.circle(img, circulo_exterior, radio_exterior, (0, 255, 255), -1)

# - Dibujar círculo interior amarillo
circulo_interior = (300, 300)
radio_interior = 100
cv.circle(img, circulo_interior, radio_interior, (0, 255, 255), -1)

# - Dibujar rectángulo rojo relleno
cv.rectangle(img, (200, 200), (400, 400), (0, 0, 255), -1)

# - Dibujar las 2 diagonales blancas (X)
cv.line(img, (200, 200), (400, 400), (255, 255, 255), 5)
cv.line(img, (400, 200), (200, 400), (255, 255, 255), 5)

# - Colocar 8 círculos verdes alrededor del centro a distancia 140 (usa sin/cos o simetrías)
centro = (300, 300)
distancia = 140
for i in range(8):
    angle = i * math.pi / 4  # Ángulo en radianes (45 grados entre círculos)
    x = int(centro[0] + distancia * math.cos(angle))
    y = int(centro[1] + distancia * math.sin(angle))
    cv.circle(img, (x, y), 20, (0, 255, 0), -1)


# - Escribir el texto "SECTOR-9" en la parte baja
cv.putText(img, "SECTOR-9", (250, 550), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# - Guardar como m3_sello_forjado_v2.png
cv.imwrite('m3_sello_forjado_v2.png', img)
# - Mostrar la imagen final
cv.imshow('Sello Biometrico Forjado', img)
cv.waitKey(0)
cv.destroyAllWindows()


````


### Misión 4
- Máscara Cyan:

![](../Pictures/Screenshots/m4_mask_cyan.png)


- Código:

````python

img = cv.imread("C:\\Users\\ameti\\Pictures\\m4_ruido 1.png")

# TODO:
# - Definir kernel promedio 3x3 (float32) y aplicar cv2.filter2D
kernel = np.ones((3, 3), dtype=np.float32) / 9
img_suavizada = cv.filter2D(img, -1, kernel)
# - Convertir a HSV con cv2.cvtColor
img_hsv = cv.cvtColor(img_suavizada, cv.COLOR_BGR2HSV)
# - Definir límites low/high para Cyan
lower_cyan = np.array([80, 100, 100])
upper_cyan = np.array([100, 255, 255])
# - Crear máscara con cv2.inRange
mask_cyan = cv.inRange(img_hsv, lower_cyan, upper_cyan)
# - Guardar máscara como m4_mask_cyan.png
cv.imwrite('m4_mask_cyan.png', mask_cyan)
#Mostrar la máscara
cv.imshow('Mascara Cyan', mask_cyan)    
cv.waitKey(0)
cv.destroyAllWindows()



````



### Misión 5
- Evidencia tricolor:




- Mensaje recuperado:

![](../Pictures/Screenshots/m5_mensaje.png)


- Código:

```
# TODO GENERACIÓN (m5_tricolor.png):
# - Crear imagen 300x700 con ruido aleatorio en BGR
img = np.random.randint(0, 256, (300, 700, 3), dtype=np.uint8)

# - Escribir el mensaje con una “tinta tramposa” (elige un color que dependa fuerte de 1 canal)
cv.putText(img, "CANAL B", (50, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
cv.putText(img, "CANAL G", (50, 200), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
cv.putText(img, "CANAL R", (50, 300), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
# - Guardar como m5_tricolor.png
cv.imwrite('m5_tricolor.png', img)

# TODO RECUPERACIÓN:
# - Separar canales: b, g, r = cv2.split(img)
b, g, r = cv.split(img)
# - Probar: canal b, canal g, canal r
cv.imshow('Canal B', b)
cv.imshow('Canal G', g)
cv.imshow('Canal R', r)
cv.waitKey(0)
cv.destroyAllWindows()
# - Probar combinaciones: cv2.absdiff(g, b) y/o (r - g) con saturación
mensaje_recuperado = cv.absdiff(g, b)

# - Umbralizar (fijo u Otsu) para que el texto sea legible
_, mensaje_umbralizado = cv.threshold(mensaje_recuperado, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# - Mostrar el mensaje recuperado
cv.imshow('Mensaje Recuperado', mensaje_umbralizado)
cv.waitKey(0)
cv.destroyAllWindows()
# - Guardar la mejor como m5_mensaje.png
cv.imwrite('m5_mensaje.png', mensaje_umbralizado)


````


---
## Análisis del Analista (Reflexiones Finales)

1. **Operadores puntuales (M1):** ¿Qué diferencia visual hay entre recuperar con multiplicación (x50) y recuperar con suma (+50)? ¿Cuál preserva mejor el contraste del texto?

> La multiplicación preserva y mejora mucho mejor el contraste del texto. En imágenes subexpuestas,multiplicar  "estira" a lo largo de todo el rango de 0 a 255, permitiendo que nuestro ojo (o un OCR) detecte las formas más fácilmente.

2. **Transformaciones geométricas (M2):** ¿Por qué es importante escoger el centro correcto al rotar una imagen con `getRotationMatrix2D`?


> El centro correcto garantiza que la transformación sea puramente de orientación y no introduzca una traslación parásita que te obligue a "perseguir" la imagen por todo el lienzo para volver a acomodarla.

3. **Convolución (M4):** ¿Por qué un filtro promedio puede ayudar a reducir falsos positivos antes de segmentar por HSV, y qué desventaja tiene sobre los bordes del texto?

> La segmentación por HSV (Hue, Saturation, Value) funciona analizando cada píxel de forma individual. Si tu imagen tiene "ruido" (puntos de color aleatorios causados por el sensor o la mala iluminación), estos píxeles aislados pueden caer dentro del rango de color que buscas (por ejemplo, el amarillo del texto) aunque no pertenezcan al objeto real.

4. **Canales (M5):** ¿Por qué separar canales puede revelar información que en la imagen a color “no se ve” a simple vista?

> En una imagen a color, un objeto rojo sobre un fondo oscuro puede parecer muy obvio, pero si el valor de intensidadde ese rojo es igual al del fondo, para un algoritmo que busca bordes, el objeto es invisible.