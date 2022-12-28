from PIL import Image
from pytesseract import pytesseract
import os

def script():
    with open(f'Roshidere.txt', 'a') as f:
        f.write('% Roshidere Volume 4.5\n')
        f.write('% By stooboie\n')
        path_to_tesseract = r'C:\Users\amrit\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
        for i in range(1,8):
            f.write(f'# Chapter {i}\n')
            files = os.listdir(f'./Chapter {i}/')
            pytesseract.tesseract_cmd = path_to_tesseract
            for j in files:
                img = Image.open(f'./Chapter {i}/{j}')
                text = pytesseract.image_to_string(img)
                if text == '':
                    f.write(f'[masha best {i}](./Chapter {i}/{j})\n')
                f.write(text)
            f.write('Chapter complete.\n')
    print('Scripting complete. Output is Roshidere.txt')
