import concurrent.futures
from PIL import Image
from pytesseract import pytesseract
import os
import sys
import subprocess
import time

os.remove('Roshidere.txt') if os.path.exists('Roshidere.txt') else None
os.remove('Roshidere.epub') if os.path.exists('Roshidere.epub') else None
print('Deleted existing files. Starting script.')

def script(num):
    for i in range(1, num + 1):
        with open(f'/Converted/{num}.txt')