from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://tekno.kompas.com/gadget"

driver = webdriver.Chrome()
driver.get(url)                   

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

data = soup.find_all("div", class_="latest--news mt2 clearfix")  

print(data)

driver.quit()