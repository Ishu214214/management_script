
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
options.set_preference("general.useragent.override", user_agent)

driver = webdriver.Firefox(options=options) 
driver.get('https://www.amazon.in/s?k=mobile')

soup= BeautifulSoup(driver.page_source ,'html.parser')
product_page_1= soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')
product_page_1_1 =product_page_1.find_all('img', class_='s-image' )
#print(product_page_1_1)
print((len(product_page_1_1)))


driver.close() 
