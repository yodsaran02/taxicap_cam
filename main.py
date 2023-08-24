import cv2
import numpy as np
cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()
    
    #cv2.imshow('video', frame)
    import test_capture
    import corner 
    import line
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
