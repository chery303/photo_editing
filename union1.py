import os
from os.path import join, getsize
import pathlib
from pathlib import Path
import time
import shutil


directory1 = '/mnt/hdd1/photos/photo_mix1'
directory2 = '/mnt/hdd1/photos/photo_mix2'
#path_list1 = Path('/mnt/hdd1/photos/', "_1_list.txt")
#path_list2 = Path('/mnt/hdd1/photos/', "_2_list.txt")

path_list1 = Path(directory1, "1_list.txt")
path_list2 = Path(directory2, "2_list.txt")

path_del_list = Path('/mnt/hdd1/photos/photo_mix1', "un1_errors.txt")

photos_list1 = open(path_list1, 'r')
photos_list2 = open(path_list2, 'r')
del_list = open(path_del_list, 'w')
count_all = 0
count_del = 0

lines1 = photos_list1.readlines()
lines2 = photos_list2.readlines()

for line1 in lines1:

    count_all += count_all

    #print(line1)
    line1_1 = line1.split(' new:')
    #print(line1_1[0])
    line1_2 = line1_1[0].split('/')
    old_name_file1 = line1_2[-1]
    #print(old_name_file1)
    new_name_file1 = line1_1[1]
    #print(new_name_file1)
    search_name = old_name_file1 + " new:" + new_name_file1


    retrieved_elements = list(filter(lambda x: search_name in x, lines2))
    if len(retrieved_elements) == 1:
        path_del_file = Path(directory1, new_name_file1)

        if os.path.isfile(path_del_file):
            os.remove(path_del_file)
            del_list.writelines("del:" + path_del_file + '\n')
            count_all += count_all
            print('-----del ' + count_del)

    print('all ' + count_all)


photos_list1.close()
photos_list2.close()
del_list.close()

print("The end")
print('del = ' + count_del)
print('all = ' + count_all)

