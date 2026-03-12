import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\ameti\\Pictures\\FFDP Skull.png')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_green= np.array([0,60,60])
upper_green= np.array([1,255,255])

lower_green1= np.array([170,60,60])
upper_green1= np.array([180,255,255])


mask = cv.inRange(hsv,lower_green,upper_green)
mask2 = cv.inRange(hsv,lower_green1,upper_green1)


result= cv.bitwise_and(img,img,mask=mask)


cv.imshow('Mascara',mask)
cv.imshow('img', img)
cv.imshow('Mascara2',mask2)
cv.waitKey(0)
cv.destroyAllWindows

