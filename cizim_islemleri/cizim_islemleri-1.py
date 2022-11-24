import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.imshow("Pencere adı",img)
# Ekranımızın arka plan rengini siyah yapmak istiyorsak
# eksenlerden oluşan matrisimizi yazarız np.zeros kullanarak
# integer'a çevirmek için np.uint8 kullanıldı

img2 = cv2.line(img, (0,0), (512,512), (255,0,0), 6)
cv2.imshow("Cizimli Pencere", img2)
# Peki pencere üzerinde çizim yapmak istersek cv2.line() kullanırız 
# (0,0) başlangıç noktamız,
# (512,512) arış noktamız,
# (255,0,0) rengimiz,
# 6 kalınlığı


cv2.waitKey(0)
cv2.destroyAllWindows()