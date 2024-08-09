from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# VPN server IP address and port
vpn_ip = 'your_vpn_ip_address'
vpn_port = 'your_vpn_port'

# Set up proxy with the VPN
proxy = {
    'http': f'http://{vpn_ip}:{vpn_port}',
    'https': f'https://{vpn_ip}:{vpn_port}'
}

# Set up Firefox options
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
options.set_preference("general.useragent.override", user_agent)

# Set up proxy for requests (for getting the HTML content)
# This step is optional if you want to fetch HTML using requests
session = requests.Session()
session.proxies.update(proxy)

driver = webdriver.Firefox(options=options)
driver.get('https://www.amazon.in/s?k=mobile')

soup = BeautifulSoup(driver.page_source, 'html.parser')

titles = soup.select('.s-line-clamp-2')
for title in titles:
    print(title.text.strip())

# Close the browser
driver.quit()
