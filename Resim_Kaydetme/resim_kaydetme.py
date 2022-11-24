import cv2

resim = cv2.imread("Resim_Okuma\yapay_zeka.jpg",0)
cv2.imshow("açılan resim",resim)
a = cv2.waitKey()
if a == 27:
    cv2.destroyAllWindows()
elif a == ord("s"):
    cv2.imwrite("yeni_resim.png",resim)