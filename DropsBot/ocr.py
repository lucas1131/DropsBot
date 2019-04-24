from PIL import Image
import pytesseract
import sys

print(pytesseract.image_to_string(Image.open(sys.argv[1])))
