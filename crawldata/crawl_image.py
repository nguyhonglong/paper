from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep
import os
import requests
import time
import re
from urllib.parse import urlparse
import csv
chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=C:\Users\nguyl\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument(r'--profile-directory=Default')
query = "ielts task 1"
driver = webdriver.Chrome(options = chrome_options)
driver.maximize_window()

driver.get('https://www.google.com/search?sca_esv=90dd98a2612e3d60&biw=1536&bih=703&sxsrf=ADLYWIIJye0mG-uO4Bz4Ldu5Fh-0HDpAIQ:1719039848962&q=bar+graph+ielts+task+1&uds=ADvngMhwMquf5yJpZEdo_SEHJVs-cJeflzMTAcZzYeV_mTeF5mJpFppvwQ-HMmaFMjmQZL-jhgTMTw_NTRAXX6jI2TLceKfO5pj57sTCpoYRmYoOYVuBhK2K6TDjlROF1jcVlpgQdUP78X6mZTRtQOr1qnv0uE7VsA&udm=2&sa=X&ved=2ahUKEwj6gbW80u6GAxUYsFYBHWkgAtcQxKsJegUIigEQAQ&ictx=0')

def scroll_to_bottom(page_number, delay_duration):
		body = driver.find_element(By.TAG_NAME, "body")
		for _ in range(page_number):
			body.send_keys(Keys.END)
			sleep(delay_duration)


scroll_to_bottom(5,1)
save_directory = "D:/paper"
os.makedirs(save_directory, exist_ok=True)
elements = driver.find_elements(By.CSS_SELECTOR, "img[id^='dimg_']")
os.makedirs('bar_chart', exist_ok=True)

for i, elem in enumerate(elements):
    img_url = elem.get_attribute('src')
    if img_url:
        try:
            response = requests.get(img_url, stream=True)
            if response.status_code == 200:
                with open(f'bar_chart/image_{i}.jpg', 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Image {i} downloaded successfully.")
            else:
                print(f"Failed to download image {i}.")
        except Exception as e:
            print(f"Error downloading image {i}: {e}")

driver.quit()