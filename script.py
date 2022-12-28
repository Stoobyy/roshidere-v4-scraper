from PIL import Image
from pytesseract import pytesseract
import os
import sys
import subprocess
import time


def script():
    with open(f'Roshidere.txt', 'a') as f:
        f.write('% Roshidere Volume 4.5\n')
        f.write("% Scrapped and EPUB'd by Stooby\n\nTranslated by [Glucose Translations](https://glucosetl.files.wordpress.com/)\n\n![cover](Cover.png)")
        path_to_tesseract = r'C:\Users\amrit\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' #change this to your tesseract path, or just change amrit to your profile name
        for i in range(1,8):
            f.write(f'\n# Chapter {i}\n')
            files = os.listdir(f'./Chapter {i}/')
            pytesseract.tesseract_cmd = path_to_tesseract
            for j in files:
                img = Image.open(f'./Chapter {i}/{j}')
                text = pytesseract.image_to_string(img)
                if text == '':
                    f.write(f'![Image {i}](Chapter {i}/{j})\n')
                f.write(text)
            f.write('\nChapter complete.\n')
    subprocess.Popen(['pandoc', 'Roshidere.txt', '-o', 'Roshidere.epub'])
    print('Scripting complete. Output is Roshidere.epub')
