import cv2 

cam = cv2.VideoCapture(0)
count = 100
i = 0
while i < 100:
    check, frame = cam.read()
    i +=1 

cv2.imwrite("test.jpg",frame)

cam.release()
#cam.destroyAllWindows()
