import cv2

# Video birden fazla karenin bir araya gelmesi
# ile oluşur bu sebepten her kareyi almak için
# bir döngü oluşturduk

#webcam kullanmak için 
yakala = cv2.VideoCapture(0)

while(True):
    deger , resimler = yakala.read()
    cv2.imshow("video",resimler)
    
    #ifin içerik mantığı klavyeden alınan tuşun 
    #hegza desimal karşılığı bize q harfini verir mi
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
    
yakala.release()
cv2.destroyAllWindows()