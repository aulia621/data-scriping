import os

def create_directory(fungsi):
    if not os.path.exists(fungsi):
        os.mkdir(fungsi)

def main_scrapper(url,directory):
    create_directory(directory)

def write_to_file(path,data):
    with open(path,'a', encoding='utf-8') as file:
        file.write(data+'\n')