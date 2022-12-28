from PIL import Image
from pytesseract import pytesseract
import os

def script():
    path_to_tesseract = r'C:\Users\amrit\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    for i in range(1,8):
        files = os.listdir(f'./Chapter {i}/')
        pytesseract.tesseract_cmd = path_to_tesseract
        for j in files:
            img = Image.open(f'./Chapter {i}/{j}')
            text = pytesseract.image_to_string(img)
            with open(f'Roshidere.txt', 'a') as f:
                f.write(f'\n\n\nCHAPTER {i}:\n\n\n')
                f.write(text)
    print('Scripting complete. Output is Roshidere.txt')