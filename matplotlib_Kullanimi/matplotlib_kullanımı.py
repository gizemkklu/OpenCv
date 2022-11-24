import cv2
from matplotlib import pyplot as plt


resim = cv2.imread("Resim_Okuma\yapay_zeka.jpg",0)
plt.imshow(resim,cmap="gray",interpolation="bicubic")
plt.xticks([])
plt.yticks([])
plt.show()