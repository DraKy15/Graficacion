# Segmentación de Frutas usando Máscara HSV


### Amet Pérez Acosta 
### N° de Control: 22121293
### Grupo B


---


## Objetivo


1. Aplicar el modelo de color HSV para segmentar objetos.
2. Analizar resultados directamente sobre una máscara binaria.
3. Identificar y contar regiones conectadas.
4. Evaluar el impacto del rango de color en la segmentación.





## Actividad 1: Exploración del Espacio HSV

+ ¿Qué ocurre cuando el rango es muy estrecho?
 
 	Se pierde la gama de colores de la imagen original.
 	
+ ¿Qué ocurre cuando el rango es muy amplio?

	La gama de colores de la imagen original se satura.
	

Código:

```python
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
```


	
Resultados:

	![](../Pictures/Screenshots/Captura de pantalla 2026-02-19 133600.png)

	![](../Pictures/Screenshots/Captura de pantalla 2026-02-19 133736.png)
	
	![](../Pictures/Screenshots/Captura de pantalla 2026-02-19 133824.png)

			



## Actividad 2: Limpieza de Ruido



+ ¿Qué tipo de ruido aparece?

El ruido que aparece es dentro de ciertas islas, contando con un relleno que antes no poseían.Además de variaciones ligeras en la iluminación y el rango definido.


+ ¿Por qué es necesario eliminarlo antes del conteo?

Porque pueden existir pixeles que son "irregulares", los cuales no forman parte del conteo real, dando falsos positivos por la fragmentación de determinadas frutas.


Código:
```python
import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\ameti\\Pictures\\frutas.png')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)


maskR1 = cv.inRange(hsv, np.array([0, 70, 50]), np.array([10, 255, 255]))
maskR2 = cv.inRange(hsv, np.array([170, 70, 50]), np.array([180, 255, 255]))
mask_roja = maskR1 + maskR2

mask_verde = cv.inRange(hsv, np.array([35, 40, 40]), np.array([85, 255, 255]))
mask_amarilla = cv.inRange(hsv, np.array([20, 100, 100]), np.array([30, 255, 255]))


def limpiar_sin_morfologia(mask):
   # Aplica un Filtro de Mediana
   
    blur = cv.medianBlur(mask, 7)
    
    num_labels, labels, stats, centroids = cv.connectedComponentsWithStats(blur, connectivity=8)
    
    # Creamos una máscara vacía para reconstruir solo lo que interesa
    mask_limpia = np.zeros_like(mask)
    
    umbral_area = 500  
    
    for i in range(1, num_labels):
        area = stats[i, cv.CC_STAT_AREA]
        if area >= umbral_area:
            mask_limpia[labels == i] = 255
            
    return mask_limpia


mask_roja_limpia = limpiar_sin_morfologia(mask_roja)
mask_verde_limpia = limpiar_sin_morfologia(mask_verde)
mask_amarilla_limpia = limpiar_sin_morfologia(mask_amarilla)

# RESULTADOS
resR = cv.bitwise_and(img, img, mask=mask_roja_limpia)
resV = cv.bitwise_and(img, img, mask=mask_verde_limpia)
resA = cv.bitwise_and(img, img, mask=mask_amarilla_limpia)

cv.imshow('Rojo (Filtro+Area)', resR)
cv.imshow('Verde (Filtro+Area)', resV)
cv.imshow('Amarillo (Filtro+Area)', resA)

cv.waitKey(0)
cv.destroyAllWindows()





```

Resultados:

```
![](../Pictures/Screenshots/Captura de pantalla 2026-02-24 161205.png)

![](../Pictures/Screenshots/Captura de pantalla 2026-02-24 161227.png)

![](../Pictures/Screenshots/Captura de pantalla 2026-02-24 161241.png)
```



## Actividad 3: Conteo de Regiones

Número total de frutas detectadas:

Frutas Rojas: 8
Frutas Amarillas: 9
Frutas Verdes: 6


Área aproximada de cada región válida:

Rojas: Alrededor de 1100 a 6800 px
Amarillas: Alrededor de 1300 a 5600 px
verdes: Alrededor de 700 a 6810 px

Código:
```python

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




```


Resultados:
```
![](../Pictures/Screenshots/Captura de pantalla 2026-02-24 181639.png)

![](../Pictures/Screenshots/Captura de pantalla 2026-02-24 181653.png)

![](../Pictures/Screenshots/Captura de pantalla 2026-02-24 181626.png)
```

## Actividad 4: Comparación de Colores


![](../Pictures/Screenshots/Captura de pantalla 2026-02-25 132955.png)


+ ¿Qué color fue más fácil segmentar?

	Rojo

+ ¿Cuál presentó más ruido?

	Verde

+ ¿Por qué?
	
	Debido a la fragmentación de ciertas partes de la 		imagen, se crean detecciones incorrectas de algunas frutas.


## Actividad 5: Análisis Crítico

 	
  1. ¿Por qué HSV es más adecuado que RGB para esta tarea?
 
 Porque permite un análisis más preciso a la hora de utilizar las máscaras, teniendo menos variaciones gracias a la luz
 
 
  2. ¿Cómo afecta la iluminación al canal V?

Se crean blancos o niveles de pureza que se pueden encontrar fuera del rango de saturación



  3. ¿Qué sucede si dos frutas tienen tonos similares?
 
Dependiendo de la máscara, puede dar resutlados que mezclen elementos en una sola



  4. ¿Qué limitaciones tiene la segmentación por color?

Se puede sufrir de falsos positivos, junto a huecos o ruido muy visible en los pixeles, siendo susceptible gracias a los cambios ambientales



# Conclusiones


Gracias a las máscaras y el uso de los rangos RGB y HSV, podemos llevar una análisis detallado de una imagen y su composición de pixeles. Siendo una herramienta clave para la corrección, mejora y descomposición de una imagen y sus capas. A través las actividades realizadas, se pudo llegar a las siguientes conclusiones:

- Superioridad del modelo HSV sobre RGB: Se comprobó que el espacio de color HSV es significativamente más robusto para la segmentación,ya que logra una mayor invarianza ante cambios de iluminación, sombras y brillos que normalmente corromperían un análisis basado solamente en canales RGB.

- Importancia del Procesamiento Morfológico: La generación de máscaras crudas suele presentar ruido de tipo "sal y pimienta" o discontinuidades en los objetos. La implementación de técnicas de apertura y cierre morfológico resultó clave para refinar las regiones de interés, eliminando falsos positivos y garantizando que cada objeto detectado mantenga su integridad estructural antes de pasar a la etapa de conteo.

- Cuantificación y Análisis de Componentes: El uso de algoritmos de etiquetado de componentes conectados transforma una simple imagen de píxeles en datos estadísticos accionables. Esta capacidad de filtrar regiones por su área permite discriminar entre el ruido residual y los objetos válidos, facilitando tareas de conteo y caracterización geométrica sin necesidad de intervención manual o validación visual constante.

