import cv2
import numpy as np
import math



image1 = cv2.imread('dave2.jpg')
gray=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
canimg = cv2.Canny(gray, 50, 200)

lines= cv2.HoughLines(canimg, 1, np.pi/180.0, 120, np.array([]))


for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(image1,(x1,y1),(x2,y2),(0,0,255),2)


cv2.imshow('Lines Detected',image1)
cv2.imshow("Canny Detection", canimg)
cv2.waitKey(0)
cv2.destroyAllWindows()