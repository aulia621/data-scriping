from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://id.indeed.com/jobs?"
params = {
    'q' : 'fresh graduate',
    'l' : 'Banyuwangi'
}
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'}
driver = webdriver.Chrome()
full_url = f"{url}&q={params['q']}&l={params['l']}"
driver.get(full_url)
html = driver.page_source

soup = BeautifulSoup(html,features='html.parser')
data = soup.find_all(name="td", attrs={'class':'resultContent'})
for i in range(len(data)):
    Pekerjaan = data[i].find("h2",{'class':'jobTitle'})
    Perusahaan = data[i].find("div",{'class':'company_location'})
    Sallary = data[i].find("div",{'class':'heading6 tapItem-gutter'})
    if Pekerjaan and Perusahaan and Sallary:
        print("Pekerjaan:" + Pekerjaan.text)
        print("Perusahaan:"+ Perusahaan.text)
        print("Sallary:"+ Sallary.text)
        print("=======================================")

print(data)
driver.quit()
