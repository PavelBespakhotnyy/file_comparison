import os
import pathlib


def files_comparison(files):
    global files_list
    files_list = {}
    for file in files:
        with open(file, 'r', encoding='UTF-8') as file_opened:
            p = pathlib.Path(file)
            name = os.path.basename(p)
            counter = 0
            for line in file_opened:
                if line != '\n':
                    counter += 1
                    files_list[name] = counter


files = ['1.txt', '3.txt', '2.txt']
files_comparison(files)

sorted_keys = sorted(files_list, key=files_list.get)

for file in sorted_keys:
    with open(file, 'r', encoding='UTF-8') as file_opened:
        data = file_opened.read()
        with open(file, 'r', encoding='UTF-8') as file_opened1:
            data1 = file_opened1.readlines()
        counter = len(data1)
        print(file, '\n', counter, '\n', data)