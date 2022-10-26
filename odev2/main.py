import cv2
import numpy as np

foto=cv2.imread("cicek.png",0)
cv2.imshow("cicek",foto)
cv2.waitKey()

max=np.max(foto)

[x,y]=np.shape(foto)

for i in range (0,x):
    for j in range (0,y):
        foto[i,j]=max-foto[i,j]

cv2.imshow("cicek",foto)
cv2.waitKey()
