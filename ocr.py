import pytesseract
import cv2
img = cv2.imread("./test1.jpg")
print(pytesseract.image_to_string(img, config='outputbase digits'))