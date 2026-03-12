import cv2 as cv
import numpy as np

#Crea una imagen de las respectivas dimensiones, con la escala modificable
#Por medio de *x 
#x= Numero entre 0 y 255
i=j=0

img2 = np.ones((400,400),np.uint8)*250
img2[220:250,220:250]=0


img2[1,1]=0

for i in range(100):
    for j in range(100):
        img2[i,j]=255-i


#Se carga desde la ubicación raiz de la imagen
#img = cv.imread('C:\\Users\\ameti\\Pictures\\Ghost.jpg')
#Se muestra en consola las dimensiones de la imagen
#print(img.shape)

#Imagen hecha
cv.imshow('img',img2)
#Wallpaper
#cv.imshow('img',img2)

cv.waitKey(0)
cv.destroyAllWindows()
