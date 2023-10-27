from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_planets_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
try:
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content, "html.parser")
    temp_list = []
    for table in soup.find_all("table", attrs={"class": "wikitable sortable jqeuery-tablesorter"}):
        tr_tags = table.find_all("tr")
except:
       scrape_more_data(hyperlink)

planet_df_1 = pd.read_csv("updated_scraped_data.csv")

# Call method
for index, row in planet_df_1.iterrows():
    scrape_more_data(row['hyperlink'])
    print(f"Data Scraping at hyperlink {index+1} completed")

# print(new_planets_data[0:10])

# Remove '\n' character from the scraped data
scraped_data = []

for row in new_planets_data:
    replaced = []
    for i in range(row):
        i = i.replace("\n", "")
        replaced.append(i)
    scraped_data.append(replaced)

print(scraped_data)

headers = ["star_name","radius", "mass", "distance_data"]

d = pd.DataFrame(scraped_data,columns = headers)

# Convert to CSV
d.to_csv('new_scraped_data.csv', index=True, index_label="id")








