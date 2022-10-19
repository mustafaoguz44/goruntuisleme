import cv2
import numpy as np

foto=cv2.imread("araba.jpg",0)
cv2.imshow("araba",foto)
cv2.waitKey()

hist= np.zeros(256)
[h,w]=np.shape(foto)
toplam=0
for i in range (0,h):
    for j in range (0,w):
        k=foto[i,j]
        hist[k]=hist[k]+1

for i in range (0,256):
    print(i,"-->",hist[i])


