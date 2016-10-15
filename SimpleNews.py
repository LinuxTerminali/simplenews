#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import webbrowser
from gtts import gTTS
from collections import Counter
import pyperclip
import validators

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
url = pyperclip.paste()
warning = 3
options = 1
while warning > 0:
    if(validators.url(url)):
        r = requests.get(url, hdr)
        content = r.text
        soup = BeautifulSoup(content, "lxml")
        website = ""
        content = ""
        for web in soup.find_all("meta"):
            if web.get("property", None) == "og:site_name":
                website = web.get("content", None)
        if Counter(website) == Counter("http://www.livemint.com/"):
            content = soup.find_all("div", {"class": "story-content"})
            website = "Livemint"
            print("Your article is from "+website)
        elif Counter(website) == Counter("The Economic Times"):
            content = soup.find_all("div", {"class": "Normal"})
            print("Your article is from "+website)
        elif Counter(website) == Counter("Quartz"):
            content = soup.find_all("div", {"class": "item-body"})
            print("Your article is from "+website)
        elif Counter(website) == Counter("Medium"):
            content = soup.find_all("div", {"class": "section-content"})
            print("Your article is from "+website)
        elif Counter(website) == Counter("Project Syndicate"):
            content = soup.find_all("div", {"class": "body"})
            print("Your article is from "+website)
        elif Counter(website) == Counter("Reuters India"):
            content = soup.find_all("span", {"id": "article-text"})
            print("Your article is from "+website)

        Qt = " "
        for p in content:
            Qt += p.getText()
            Qt = str(Qt.encode('utf-8'))
        choice = input("if you want to listen to the article press 1 or for text press 2:  ")
        if(choice == 1):
            print("It will take sometime please wait")
            tt = gTTS(text=Qt + " article was published on " + website, lang="en")
            tt.save("News.mp3")
            print("Done!")
            webbrowser.open("News.mp3")
            options = input("Press 1 to contiue or press 2 to exit: ")
            if options == 1:
                url = raw_input("Please provide another URL: ")
            else:
                warning = 0
        else:
            txt_file = open("News.txt", "w")
            txt_file.write(Qt)
            webbrowser.open("News.txt")
            print("Done!")
            txt_file.close()
            options = input("Press 1 to contiue or press 2 to exit: ")
            if options == 1:
                url = raw_input("Please provide another URL: ")
            else:
                warning = 0
    else:
        print("You have " + str(warning) + " try left ")
        url = raw_input("Please provide a valid url:  ")
        warning -= 1

if warning == 0:
    print("Thanks for using SimpleNews")
