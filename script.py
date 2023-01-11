from PIL import Image
from pytesseract import pytesseract
import os
import sys
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed
import time


def script():
    global last
    os.remove('Roshidere.txt') if os.path.exists('Roshidere.txt') else None
    os.remove('Roshidere.epub') if os.path.exists('Roshidere.epub') else None
    print('Deleted existing files. Starting script.')
    with open(f'Roshidere.txt', 'a') as f:
        f.write('Roshidere Volume 4.5\n')
        f.write("Scrapped and EPUB'd by Stooby\nTranslated by [Glucose Translations](https://glucosetl.files.wordpress.com/)\n\n")
        f.write('# Illustrations\n')
        files = os.listdir('./Pictures/')
        for i in files:
            f.write(f'![Image {i}](Pictures/{i})\n')
        print('Cover image added. Starting chapter 1.')
        path_to_tesseract = r'C:\Users\amrit\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' #change this to your tesseract path, or just change amrit to your profile name
        for i in range(1,14):
            f.write(f'\n# Chapter {i}\n')
            files = os.listdir(f'./Chapter {i}/')
            # pytesseract.tesseract_cmd = path_to_tesseract
            for j in files:
                # img = Image.open(f'./Chapter {i}/{j}')
                # text = pytesseract.image_to_string(img)
                # if text == '':
                f.write(f'![Image {i}](Chapter {i}/{j})\n')
            f.write('\nChapter complete.\n')
            print(f'Chapter {i} complete.')
            last = i
        run()

def run():
    subprocess.Popen(['pandoc', 'Roshidere.txt', '-o', 'Roshidere.epub', '--epub-cover-image', 'Cover.png', '--metadata', 'title="Roshidere Volume 4.5"'])
    print('Scripting complete. Output is Roshidere.epub')
    time.sleep(10)
    webhook()

def webhook(last = 13):
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1058597249770340352/QMg9jatnnBbbrqVZmk7oZNvUyw43wDUl3eRKVWtvCQlmstRPlWUQI3N5S5It4TKTcvvG', username="Roshidere Updater")
    embed = DiscordEmbed(title='Update', description=f'Roshidere Volume 4.5 Chapters 1-{last} Black And White', color=242424)
    embed.set_timestamp()
    embed.set_footer(text='Made by Stooby with <3')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/971761146325532712/1058599268396576848/Cover.png?width=408&height=583')
    with open("Roshidere.epub", "rb") as f:
        webhook.add_file(file=f.read(), filename='Roshidere.epub')
    webhook.add_embed(embed)
    response = webhook.execute()
    print('Discord webhook sent.')
