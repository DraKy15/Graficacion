import cv2 as cv
import numpy as np 


img = np.ones((500,500), np.uint8)*115


#Generar un rebote de la pelota dentro del cuadrado
def rebote_pelota(pos, vel, radio, img_size):
    x, y = pos
    vx, vy = vel
    w, h = img_size
    
    # Actualiza la posición
    x += vx
    y += vy
    
    # Verifica colisiones con las paredes
    if x - radio < 0:  
        x = radio
        vx = -vx  
    elif x + radio > w:  
        x = w - radio
        vx = -vx 
        
    if y - radio < 0:  
        y = radio
        vy = -vy  
    elif y + radio > h: 
        y = h - radio
        vy = -vy  
        
    return (x, y), (vx, vy)  

pos = (250, 250)
vel = (5, 3)
for i in range(500):
    
    pos, vel = rebote_pelota(pos, vel, 20, (500, 500))
    cv.circle(img, (int(pos[0]), int(pos[1])), 20 , (255, 0, 0), -1 )

    cv.imshow('img', img)
    img = np.ones((500,500,3), np.uint8)*150 
    cv.waitKey(10)


cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()