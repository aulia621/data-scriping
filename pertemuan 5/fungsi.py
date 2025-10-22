import os

def create_directory(scrapping):
    if not os.path.exists(scrapping):
        os.mkdir(scrapping)

def main_scrapper(url,directory):
    create_directory(directory)