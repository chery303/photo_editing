
'''
в разработке

удаление файлов по списку
'''



from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime
import pathlib
from pathlib import Path
import os
from os.path import join, getsize
import time


directory = 'I:\\src_all'

path_del_list = Path(directory, "del_list.txt")
path_complete_list = Path(directory, "complete_list.txt")

del_list = open(path_del_list, 'r')
complete_list = open(path_complete_list, 'w')
count = 0
count_trash = 0

for line in del_list:

    count += 1
    print(str(count) + ' ' + line[0:-1])
    os.remove(line[0:-1])

    complete_list.writelines(str(count) + ' === ' + line + '\n')

print("The end")
print('delete = ' + str(count))
print('err = ' + str(count_trash))
