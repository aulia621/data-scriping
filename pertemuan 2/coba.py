import os

def create_dictory(Scraping):
    if not os.path.exists(Scraping):
        os.mkdir(Scraping)

create_dictory("Scraping")

def create_new_file(path):
    f=open(path,'w')
    f.write("")
    f.close()

create_new_file("Scraping/test.txt")

def clear_file(path):
    f = open(path,'w')
    f.close()

clear_file("Scraping/test.txt")

import os

def does_file_exist(path):
    return os.path.isfile(path)

print (does_file_exist("Srcaping/test.txt"))

def create_new_file(path):
    f=open(path,'w')
    f.write("")
    f.close()

def write_to_file(path,data):
    with open(path,'a') as file:
        file.write(data +'\n')

def read_data(path):
    with open(path,'rt') as file:
        for line in file:
            print(line)

create_new_file("scraping/file.txt")
write_to_file("scraping/file.txt","this is a line")
write_to_file("scraping/file.txt","this is a line")

read_data("scraping/file.txt")

def remove_file(path):
    if does_file_exist(path):
        os.remove(path)
    else:
        print("file tidak ada")

remove_file("scraping/file1.txt")



