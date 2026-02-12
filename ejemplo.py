import cv2 as cv
import numpy as np

#Crea una imagen de las respectivas dimensiones, con la escala modificable
#Por medio de *x 
#x= Numero entre 0 y 255
img2 = np.ones((400,400),np.uint8)*14

#Se carga desde la ubicación raiz de la imagen
img = cv.imread('C:\\Users\\ameti\\Pictures\\Ghost.jpg')
#Se muestra en consola las dimensiones de la imagen
print(img.shape)

#Imagen hecha
cv.imshow('img2',img)
#Wallpaper
cv.imshow('img',img2)

cv.waitKey()
cv.destroyAllWindows()
