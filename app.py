# dev - rithin

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
from datetime import date
import webbrowser
import os

# python -m venv venv
# venv\Scripts\activate.bat
# python app.py

url = "https://news.google.com/search?q=bosch%20site%3Athehindu.com%20when%3A1y&hl=en-IN&gl=IN&ceid=IN%3Aen" #google news url

# ========== LocalHost Settings ========== #
options = Options()
options.headless = True #headless selenium
service_obj = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, chrome_options=options)

driver.get(url)
time.sleep(5)

newsHeading = driver.find_elements(By.CSS_SELECTOR, "h3.ipQwMb.ekueJc.RD0gLb") #news content selector
newsLink = driver.find_elements(By.CSS_SELECTOR, "h3.ipQwMb.ekueJc.RD0gLb > a") #news link selector

totalLen = len(newsHeading)

data = []
today = str(date.today())

with open("data.json", "r+") as outfile:
    x=0
    while x!= totalLen:
        newsHeadingX = newsHeading[x].get_attribute('innerText')
        newsLinkX = newsLink[x].get_attribute('href')

        check = newsHeadingX.lower()

        if check.find('bosch') != -1:
            data += [
                {
                    "newsHeading": newsHeadingX,
                    "newsLink": newsLinkX,
                    "date": today
                }
            ]

        x+=1
    
    # Saving Json Data
    file_data = json.load(outfile)
    file_data["data"].append(data)
    outfile.seek(0)
    json.dump(file_data, outfile, indent = 4)

webbrowser.open_new_tab('http://127.0.0.1:8000/')
os.system("python3 -m http.server")