import cv2
import time
cam = cv2.VideoCapture(0)
i=0
time.sleep(1)
while True:
    check, img = cam.read()
    if check:
        cv2.imwrite("trained/"+str(i)+".jpg")
    time.sleep(1)
    