
'''
в разработке

список файлов в папке
'''


import exifread
import os
from os.path import join, getsize
import pathlib
from pathlib import Path
import time
import shutil

directory = 'I:\\src_all'

path_list1 = Path(directory, "_list_old.txt")
path_list2 = Path(directory, "_list_new.txt")


photos_list1 = open(path_list1, 'w')
photos_list2 = open(path_list2, 'w')
count = 0
count_trash = 0

for root, dirs, files in os.walk(directory):


    for file_ in files:

        file = file_.upper()


        fn, file_extension_ = os.path.splitext(file)
        file_extension = file_extension_.upper()


        if file_extension == '.THM' or file_extension == '.DB' or file_extension == '.JSON' \
                or file_extension == '.INFO' or file_extension == '.HTML' or file_extension == '.TXT' \
                or file_extension == '.DTHUMB':
            continue

        count += 1
        photos_list1.writelines(str(count) + " s:" + root + "\\" + file_ + '\n')
        photos_list2.writelines(str(count) + " s:" + file + '\n')

    print("The end")
    print('files = ' + str(count))
