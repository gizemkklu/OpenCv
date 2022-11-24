import numpy as np
import cv2

resim = cv2.imread("Resim_Okuma\yapay_zeka.jpg",0)
cv2.imshow("yapay zeka",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()