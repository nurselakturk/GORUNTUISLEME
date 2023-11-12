import cv2
import numpy as np

resim=cv2.imread("../histogram hesaplama/resim1.jpg")
#imread=resim değişkeninin içine resim1 i atar
resim1=cv2.imread("../histogram hesaplama/resim1.jpg", 0)
#0 koyarak resmi grileştirdik.siyah beyaz resim oldu.resmin kanal sayısı 1 olur.
cv2.imshow("muhammedali",resim)
#imshow resmi açar
cv2.waitKey(0)
#waitkey kapanışta kullanılması gerekir.pencere açıldığında pencerenin kapanması için herhangi bir tuşa basılmasını bekler.
cv2.destroyAllWindows()
#desroyallwindows opencvye bağlı tüm pencerelerin kapanmasını sağlar
print(resim)
#bize resimdeki her bir pikselin matrissel görünümünü verir.
print(resim.size)
#size resmin boyutunu verir.
print(resim.dtype)
#resmin data tipini verir.her pikselin kaç bit olduğunu verir.
print(resim.shape)
#genişliğini,yüksekliğini ve kaç kanaldan oluştuğunu verir.
print(resim[(230,80)])
#bir resmin herhangi ir pikselinin BGR değerini bize verir.
print("resmin boyutu: "+str(resim.size))
#yazı ekleyip istenen şeyi string olarak yazdırmak.
B=resim[:,:,0]
G=resim[:,:,1]
R=resim[:,:,2]
#BGR değerlerini öğrenmenin ve değikenlere atamanın bir yolu.0,1,2 kaçıncı kanal olduğu.
cv2.imshow("mavi: ",B)
cv2.imshow("yeşil: ",G)
cv2.imshow("kırmızı: ",R)
cv2.waitKey()






