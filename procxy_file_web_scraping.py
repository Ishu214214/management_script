from selenium import webdriver
from bs4 import BeautifulSoup
import time
options = webdriver.FirefoxOptions()
options.headless = True
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
options.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(options=options)
driver.get("https://www.amazon.in/dp/B0CSJRH41L")
time.sleep(4)
soup = BeautifulSoup(driver.page_source, 'html.parser')
link = soup.find('div', class_='a-fixed-left-grid')
# Write the entire prettified HTML to a file
with open("copy1.html", 'wt', encoding='utf-8') as file:
    file.write(soup.prettify())