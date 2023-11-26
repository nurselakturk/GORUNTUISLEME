import cv2
import numpy as np
from matplotlip import pyplot as plt

resim = cv2.imread("rise.jpg")
gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
e,thresh1= cv2.threshold(gri,120,255, cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
cont,a=cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
rgb = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb,cont,-1,(0,255,0),2)
cv2.imshow("Bınary",gri)
cv2.imshow("thresh", thresh1)
cv2.imshow("opening", opening)
cv2.imshow("cont", rgb)
print("pirincsayısı:",len(cont))
cv2.waitKey(0)
cv2.destroyAllWindows()