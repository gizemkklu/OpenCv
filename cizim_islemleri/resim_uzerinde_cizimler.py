import cv2
# Resim üzerinde çizim yapalım
img = cv2.imread("Resim_Okuma\yapay_zeka.jpg")

# Dikdörtgen çizdirdik
img2 = cv2.rectangle(img, (15,15), (1670,1100),(0,0,255),6)

# Daire çizdirdik 
# Merkez noktası ve çapı belirledik(120) ve dairemiz tamamlandı
img3 = cv2.circle(img2, (700,400),120,(255,0,0),4)
# cv2.imshow("Çember çizimi",img3)

# Resim üzerine yazı yazdıralım
font = cv2.FONT_HERSHEY_COMPLEX
img4 = cv2.putText(img3, "Yazi" ,(400,200), font , 4, (250,55,66), 4 ,cv2.LINE_AA)
cv2.imshow("Resimde yazı",img4)


cv2.waitKey(0)
cv2.destroyAllWindows()