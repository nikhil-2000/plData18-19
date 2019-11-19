import cv2
import numpy as np


img = cv2.imread('Liverpool_FC.PNG')

#print(img)
rTotal = 0
gTotal = 0
bTotal = 0
pxTotal = 0


for row in img:
    for px in row:
        r, g, b = px

        allWhite = r + g + b == 200*3
        allBlack = r + g + b == 100
        if not allWhite and not allBlack:
            pxTotal += 1
            rTotal += r
            gTotal += g
            bTotal += b

print(r,g,b,pxTotal)

r = int(rTotal/pxTotal)
g = int(gTotal/pxTotal)
b = int(bTotal/pxTotal)

col = [r,g,b]

print(col)