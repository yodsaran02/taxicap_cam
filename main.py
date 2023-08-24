import cv2
import numpy as np
cam = cv2.VideoCapture(0)

while True:
    check, frame = cam.read()

    cv2.imshow('video', frame)
    	
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    alpha = np.sum(frame, axis=-1) > 0

    # Convert True/False to 0/255 and change type to "uint8" to match "na"
    alpha = np.uint8(alpha * 255)

    # Stack new alpha layer with existing image to go from BGR to BGRA, i.e. 3 channels to 4 channels
    result = np.dstack((frame, alpha))

    # Save result   
    cv2.imshow('alpha', result)
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
