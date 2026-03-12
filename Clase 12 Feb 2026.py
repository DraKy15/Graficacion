import cv2 as cv
import numpy as np


"""
img1 =cv.imread('C:\\Users\\ameti\\Pictures\\FFDP Skull.png')
img1a = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
x,y =img1.shape
img2= np.zeros((x,y),np.uint8)

for i in range(x):
    for j in range(y):
        img2=255-img1a[i,j]
        if(img1[i,j]>150):
            img2[i,j]=255
        else:
            img2[i,j]=0


"""
img1 = cv.imread('C:\\Users\\ameti\\Pictures\\FFDP Skull.png')
x,y,z =img1.shape
print(x,y,z)
img2= np.zeros((x,y),np.uint8)
b,g,r=cv.split(img1)
mr= cv.merge([img2,img2,r])
mg= cv.merge([img2,g,img2])
mb= cv.merge([b,img2,img2])

nueva = cv.merge([r,g,b])
nueva2 = cv.merge([g,b,r])
nueva3 = cv.merge([b,g,r])

cv.imshow('n1',nueva)
cv.imshow('n2',nueva)
cv.imshow('n3',nueva)

cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)

cv.imshow("imagen",img1)
cv.waitKey(0)
cv.destroyAllWindows()
