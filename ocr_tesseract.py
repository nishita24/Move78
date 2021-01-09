import cv2 
import os 
import pytesseract 
from PIL import Image 

img = cv2.imread('DEVRAJ_DEVADIGA_ABFLMUMPL0000036110_KYC_APP-6.jpg')
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

filename = "{}.jpg".format(os.getpid()) 
cv2.imwrite(filename, gray) 
text = pytesseract.image_to_string(Image.open(filename)) 
os.remove(filename) 
print(text) 

file = open("output.txt", "w")
file.write(text)
file.close()
