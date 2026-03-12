import cv2 as cv
import numpy as np 


#Hace dibujo con estas figuras sin utilizar for


img = np.ones((500,500), np.uint8)*200


#Base de la casa
cv.rectangle(img, (150,250), (350,450), (100,56,0), -1)

#Techo de la casa
techo = np.array([[150,250], [350,250], [250,150]], np.int32)
puntos_techo = techo.reshape((-1,1,2))
cv.polylines(img, [puntos_techo], True, (0,0,255), 3)

#Puerta de la casa
cv.rectangle(img, (230,350), (270,450), (0,0,255), -1)

#Ventanas de la casa
cv.rectangle(img, (170,300), (210,350), (255,255,255), -1)
cv.rectangle(img, (290,300), (330,350), (255,255,255), -1)





cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()