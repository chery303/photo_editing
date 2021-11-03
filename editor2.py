import os
from os.path import join, getsize
import pathlib
from pathlib import Path
import time
import shutil


directory = '/mnt/hdd1/photos/фото_актуальное_это_заполнять'
directory2 = '/mnt/hdd1/photos/photo_mix2'
path_list = Path(directory2, "_list.txt")
path_errors_list = Path(directory2, "_errors.txt")


photos_list = open(path_list, 'w')
errors_list = open(path_errors_list, 'w')
count = 0
count_trash = 0

for root, dirs, files in os.walk(directory):


    for file_ in files:

        file = file_.upper()
        count += 1
        #if count == 300:
        #    break

        _path = Path(root, file_)  # not upper
        fn, file_extension_ = os.path.splitext(file)
        file_extension = file_extension_.upper()

        if file_extension == '.THM' or file_extension == '.DB' or file_extension == '.JSON' \
                or file_extension == '.INFO' or file_extension == '.HTML':
            count -= 1
            count_trash += count_trash
            continue

        _time = time.gmtime(os.path.getmtime(_path))
        _new_name = time.strftime("%Y-%m-%d %H-%M-%S", _time) + file_extension
        _new_path = Path(directory2, _new_name)

        check_file = os.path.isfile(_new_path)
        if check_file == False:

            #write line to the list.txt and copy file
            photos_list.writelines("s:" + root + "/" + file + " new:" + _new_name + '\n')
            shutil.copy2(_path, _new_path)

        else:
            _new_name = time.strftime("%Y-%m-%d %H-%M-%S", _time) + "_" + file
            _new_path = Path(directory2, _new_name)

            photos_list.writelines("s:" + root + "/" + file + " new:" + _new_name + '\n')
            shutil.copy2(_path, _new_path)

            errors_list.writelines("err s:" + root + "/" + file + " new:" + _new_name + '\n')
            #print('****************' + str(count) + " " + root + "/" + file + " " + _new_name)


        print(str(count) + " " +  root + "/" + file + " " + _new_name)


    else:
        continue
    break

photos_list.close()
errors_list.close()

print("The end")
print('transmit = ' + str(count))
print('trash = ' + str(count_trash))
count_all = count + count_trash
print('all = ' + str(count_all))
