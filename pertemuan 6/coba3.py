from bs4 import BeautifulSoup
import os
import fungsi
import requests
# soup = BeautifulSoup('<html><body><div class="class1">''</div><div class="class2"></div><div class="class3"></div></body></html>')
# soup.findAll(True, {"class":["class1", "class2"]}) #mencari tag apapun (ga peduli div,p selama classnya sama)
def main_scraper(url,directory,file):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text,"html.parser")
    # articles = soup.find_all("h3",{'class':'article__title article__title--medium'})
    # articles2 = soup.find_all(True,{'class':['article__box','article__title']})
    articles = soup.find_all(True,{'class':['article__box', 'article__title']})

    # for article in articles:
    #     print("URL : " + article.a.get("href"))
    #     print("judul : " + article.text)
    #     print()
    # for article2 in articles2:
    #     print("URL2 : " + article2.a.get("href"))
    #     print("judul2 : " + article2.text)
    #     print()
    for article in articles:
        print("URL : " + article.a.get("href"))
        print("judul : " + article.text)
        file_path = os.path.join(directory, file)
        fungsi.write_to_file(file_path, "URL: " + article.a.get("href"))
        fungsi.write_to_file(file_path, "Judul: " + article.a.text + "\n")
    
# def read_data(path):
#     with open(path,'rt') as file:
#         for line in file:
#             print(line)

# def write_to_file(path,data):
#     with open(path,'a') as file:
#         file.write(data +'\n')

# write_to_file("hasil/hasil.txt","Hasil")
# read_data("hasil/hasil.txt")
main_scraper("https://tekno.kompas.com/gadget","Hasil5", "hasil.txt")