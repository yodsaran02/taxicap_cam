import numpy as np
import cv2 as cv

while True:
    cam = cv.VideoCapture(0)
    check, img = cam.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 2, 3, 0.04)

    dst = cv.dilate(dst, None)

    img[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv.imshow('dst', img)
    cam.release()
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()
