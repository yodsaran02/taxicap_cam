import pytesseract
import Image
img = Image.open("./test,jpg")
pytesseract.image_to_string(img, config='outputbase digits')