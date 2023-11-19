import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while(True):
    ret, bilgkamerasi = kamera.read()

    hsv = cv2.cvtColor(bilgkamerasi, cv2.COLOR_BGR2HSV)

    alt_kirmizi = np.array([0,100,100])
    ust_kirmizi = np.array([10,255,255])

    maske = cv2.inRange(hsv, alt_kirmizi, ust_kirmizi)

    maskeli_goruntu = cv2.bitwise_and(bilgkamerasi,bilgkamerasi, mask=maske)

    cv2.imshow('Orjinal Goruntu (Bilgisayar Kamerasi)',bilgkamerasi)
    cv2.imshow('maskelenmiş goruntu (Bilgisayar Kamerasi',maskeli_goruntu)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

kamera.release()
cv2.destroyAllWindows()

