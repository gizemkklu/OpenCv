import cv2

yakala = cv2.VideoCapture("video_okuma/video1.mp4")

# Genişliği almak
print(yakala.get(cv2.CAP_PROP_FRAME_WIDTH))
# Yüksekliği almak
print(yakala.get(cv2.CAP_PROP_FRAME_HEIGHT))


while(yakala.isOpened()):
    deger, frame = yakala.read()
    frame = cv2.rectangle(frame,(500,200) ,(600,300),(0,255,0),5)
    cv2.imshow("video",frame)
    
    if(cv2.waitKey(1) & 0XFF == ord("q")):
        break
yakala.release()
cv2.destroyAllWindows()