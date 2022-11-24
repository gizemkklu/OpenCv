import cv2
import numpy as np


#buradaki yakala olarak belirttiğimiz
# yakalaya her zaman döngüde ulaşılamaya bilir
# ve döngüde belittiğimiz deger = 0' a eşitlenir
#bunun olmaması için 
yakala  = cv2.VideoCapture("video_okuma/video1.mp4")

# eğer yakala değişkeni açıldıysa döngüye gir
while(yakala.isOpened()):
    deger , kareler = yakala.read()
    gray = cv2.cvtColor(kareler, cv2.COLOR_BGR2GRAY)
    cv2.imshow("djkfhks", gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
yakala.release()
cv2.destroyAllWindows()