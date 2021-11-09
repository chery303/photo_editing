
'''
Перенос файлов формата AVI, у которых выставлена дата Creation date:
Имя нового файла создается из даты и старого имени файла
Полсе переноса старый файл удаляетс
Отработано на основной папке
'''


import exifread
import os
from os.path import join, getsize
import pathlib
from pathlib import Path
import time
import shutil

from hachoir.parser import createParser
from hachoir.metadata import extractMetadata


def creation_date(filename):
    parser = createParser(filename)
    metadata = extractMetadata(parser)
    return metadata.get('creation_date')

directory = 'I:\\test'
directory2 = 'I:\\dst2'
path_list = Path(directory, "_list.txt")
path_errors_list = Path(directory, "_errors.txt")
path_del_list = Path(directory, "del_list.txt")

photos_list = open(path_list, 'w')
errors_list = open(path_errors_list, 'w')
del_list = open(path_del_list, 'w')
count = 0
count_trash = 0

for root, dirs, files in os.walk(directory):


    for file_ in files:

        file = file_.upper() # upper
        count += 1

        _path = Path(root, file_)  # not upper
        fn, file_extension_ = os.path.splitext(file)
        file_extension = file_extension_.upper()

        if '9908.AVI' in file:
            continue

        if file_extension == '.THM' or file_extension == '.DB' or file_extension == '.JSON' \
                or file_extension == '.INFO' or file_extension == '.DTHUMB':
            os.remove(_path)

        if file_extension == '.THM' or file_extension == '.DB' or file_extension == '.JSON' \
                or file_extension == '.INFO' or file_extension == '.HTML' or file_extension == '.TXT' \
                or file_extension == '.ZIP' or file_extension == '.PPTX' or file_extension == '.INI' \
                or file_extension == '.JPG' or file_extension == '.GIF':

            #or file_extension == '.MP4'
            #or file_extension == '.AVI' or file_extension == '.3GP' or file_extension == '.DTHUMB'


            count -= 1
            count_trash += 1
            errors_list.writelines(str(count_trash) + " s:" + root + "\\" + file + '\n')
            continue


        try:
            _path_str = root + '\\' + file_
            d = creation_date(_path_str)

            if d != 1:

                #print(d)
                #print(type(d))
                old_file_name = ''
                #if file[0:3] == 'IMG' or file[0:3] == 'DSC' or file[0:3] == 'XMG' or file[0:3] == 'CIM' or file[0:3] == 'ФОТ':
                old_file_name = '_' + file



                new_file_name = str(d).replace(':', '-') + old_file_name

                #чтобы не было файлов без расширения
                if old_file_name == '':
                    new_file_name += file_extension



                _new_path = Path(directory2, new_file_name)


                check_file = os.path.isfile(_new_path)
                if check_file == False or (check_file == True and old_file_name != ''):
                    #нет файла с датой или
                    #есть файл с датой и признанным названием
                    #перезапишем
                    print(_new_path)
                    shutil.copy2(_path, _new_path)
                    #os.remove(_path)
                    photos_list.writelines(str(count) + " s:" + root + "\\" + file + " ===>:" + new_file_name + '\n')
                    del_list.writelines(root + "\\" + file_ + '\n')

                elif check_file == True and old_file_name == '':
                    #есть файл с такой датой, но без признанного названия
                    #нужно проверить непризнанное название после даты
                    #делаем название файла из даты + старое название и записываем
                    #а если уже есть такой, то перезаписываем
                    new_file_name2 = str(d).replace(':', '-') + '_' + file
                    _new_path2 = Path(directory2, new_file_name2)
                    print(_new_path2)
                    shutil.copy2(_path, _new_path2 + '\n')
                    #os.remove(_path)
                    photos_list.writelines(str(count) + " s:" + root + "\\" + file + " ===>:" + new_file_name2 + '\n')
                    del_list.writelines(root + "\\" + file_ + '\n')


            else:
                count_trash += 1
                errors_list.writelines("*** " + str(count_trash) + " s:" + root + "\\" + file + '\n')

        except:
            count_trash += 1
            errors_list.writelines("!!!!! " + str(count_trash) + " s:" + root + "\\" + file + '\n')





        print(str(count) + ' ' + str(file_))


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