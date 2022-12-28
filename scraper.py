from bs4 import *
import requests
import os
import json
import re
import time
from script import script

for num in range(1,8):
    os.mkdir(f'Chapter {num}') if not os.path.exists(f'Chapter {num}') else None
    site = f'https://glucosetl.wordpress.com/roshidere-v4-5-c{num}/'
    r = requests.get(f'https://glucosetl.wordpress.com/roshidere-v4-5-c{num}/')
    soup = BeautifulSoup(r.text, "html.parser")
    image_tags = soup.find_all('img')
    urls = [img['src'] for img in image_tags]
    for url in urls:
        filename = re.search(r'/([\w_-].*(?=jpg)?w=791)', url)
        if not filename:
            continue
        name = filename.group(1).split('/')[-1].strip('?w=791')
        with open(f'Chapter {num}/{name}', 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(site, url)
            response = requests.get(url)
            f.write(response.content)
    print(f"Chapter {num} download complete, scripting starts after all chapters are complete!.")

print('Scripting started! It will take a while, please be patient as script has to download and install multiple requirements before converting.')
script()




