import cv2
import time
cam = cv2.VideoCapture(0)
i=0
time.sleep(1)
while True:
    check, img = cam.read()
    cv2.imshow("feed",img)
    if check and i%20 == 0:
        print("Saved",str(i))
        cv2.imwrite("trained/"+str(i)+".jpg",img)
    i += 1
    