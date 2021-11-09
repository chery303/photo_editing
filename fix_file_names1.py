import os
from pathlib import Path
import shutil

directory_del = 'I:\dst'
directory_srs = 'H:\фото_актуальное_это_заполнять'
directory_dst2 = 'I:\dst2'


count = 0

path_list = Path(directory_dst2, "_list.txt")
photos_list = open(path_list, 'w')
path_errors_list = Path(directory_dst2, "_del.txt")
del_list = open(path_errors_list, 'w')

path_original_list = Path(directory_dst2, "2_list.txt")
original_list = open(path_original_list, 'r')
double_list = list()

count1 = 0
count_double = 0

for line in original_list:

    if line[-5] != '.' and line[-4] != '.':
        print('----')
        count1 += 1


        del_file = line[-20:].strip()
        path_del_file = Path(directory_del, del_file)
        print(path_del_file)


        ind1 = line.find('s:I:\src_all')
        ind2 = line.find('===>')
        dir_part = line[(ind1+13):(ind2-1)]
        ind3 = dir_part.rfind('\\')
        name_copy_file = dir_part[ind3+1:]
        copy_file = directory_srs + '\\' + dir_part
        print(copy_file)

        file_extension = ''
        if copy_file[-4] == '.':
            file_extension = copy_file[-4:]
        elif copy_file[-3] == '.':
            file_extension = copy_file[-3:]

        new_file_name = del_file + file_extension
        path_new_file = Path(directory_dst2, new_file_name)




        #теперь сделаем действия с файлами

        check_file = os.path.isfile(path_new_file)
        if check_file == False:
           shutil.copy2(copy_file, path_new_file)
           photos_list.writelines(str(count) + " s:" + copy_file + " ===>:" + new_file_name + '\n')

        else: # уже есть файл с таким наименованием, добавим еще и старое название
            new_file_name = del_file + '_' + name_copy_file
            path_new_file = Path(directory_dst2, new_file_name)

            shutil.copy2(copy_file, path_new_file)
            photos_list.writelines(str(count) + " s:" + copy_file + " ===>:" + new_file_name + '\n')


        #удаляем файл без расширения
        check_file_del = os.path.isfile(path_del_file)
        if check_file_del:
            os.remove(path_del_file)
            del_list.writelines(str(count1) + " s:" + directory_del + "\\" + del_file + '\n')









