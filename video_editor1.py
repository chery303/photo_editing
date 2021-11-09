
'''

в разработке
для исправления даты видео
'''



from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime
import pathlib
from pathlib import Path
import os
from os.path import join, getsize
import time


directory = 'I:\убрать 1 год_доп папка'
#directory2 = 'I:\\test\\2'
path_list = Path(directory, "_list.txt")
path_errors_list = Path(directory, "_errors.txt")

photos_list = open(path_list, 'w')
errors_list = open(path_errors_list, 'w')
count = 0
count_trash = 0

for root, dirs, files in os.walk(directory):
    for file_ in files:

        file = file_.upper()
        count += 1
        _path = Path(root, file_)  # not upper
        fn, file_extension_ = os.path.splitext(file)
        file_extension = file_extension_.upper()

        if file_extension == '.THM' or file_extension == '.DB' or file_extension == '.JSON' \
                or file_extension == '.INFO' or file_extension == '.HTML' or file_extension == '.TXT' \
                or file_extension == '.MP4' or file_extension == '.ZIP' or file_extension == '.PPTX' \
                or file_extension == '.AVI' or file_extension == '.3GP' or file_extension == '.DTHUMB':
            count -= 1
            #count_trash += 1
            continue


        with open(_path, 'rb') as image_file:
            image_bytes = image_file.read()
            my_image = Image(image_bytes)

            if my_image.has_exif:

                #print(_path)
                #print(dir(my_image))
                datetime_original = my_image.datetime_original




                old_datetime = datetime(year=int(datetime_original[0:4]),
                                        month=int(datetime_original[5:7]),
                                        day=int(datetime_original[8:10]),
                                        hour=int(datetime_original[11:13]),
                                        minute=int(datetime_original[14:16]),
                                        second=int(datetime_original[17:]))

                new_datetime = datetime(year=int(datetime_original[0:4])-1,
                                        month=int(datetime_original[5:7]),
                                        day=int(datetime_original[8:10]),
                                        hour=int(datetime_original[11:13]),
                                        minute=int(datetime_original[14:16]),
                                        second=int(datetime_original[17:]))
                year = str(int(datetime_original[0:4]) - 1)
                print(_path)
                print(old_datetime, ' == ', new_datetime)

                my_image.datetime = new_datetime.strftime(DATETIME_STR_FORMAT)
                my_image.datetime_original = new_datetime.strftime(DATETIME_STR_FORMAT)
                my_image.datetime_digitized = new_datetime.strftime(DATETIME_STR_FORMAT)

                with open(_path, 'wb') as new_file:
                    new_file.write(my_image.get_file())


                old_name = file_
                new_name = old_name
                if '2007' in old_name:
                    new_name = old_name.replace('2007', year)
                elif '2008' in old_name:
                    new_name = old_name.replace('2008', year)
                elif '2009' in old_name:
                    new_name = old_name.replace('2009', year)
                elif '2010' in old_name:
                    new_name = old_name.replace('2010', year)
                elif '2011' in old_name:
                    new_name = old_name.replace('2011', year)
                elif '2012' in old_name:
                    new_name = old_name.replace('2012', year)
                elif '2013' in old_name:
                    new_name = old_name.replace('2013', year)
                elif '2014' in old_name:
                    new_name = old_name.replace('2014', year)
                elif '2015' in old_name:
                    new_name = old_name.replace('2015', year)
                elif '2016' in old_name:
                    new_name = old_name.replace('2016', year)
                elif '2017' in old_name:
                    new_name = old_name.replace('2017', year)
                elif '2018' in old_name:
                    new_name = old_name.replace('2018', year)
                elif '2019' in old_name:
                    new_name = old_name.replace('2019', year)




            else:
                count -= 1
                count_trash += 1
                errors_list.writelines(str(count_trash) + " s:" + root + "\\" + file + '\n')
                continue

        if old_name != new_name:
        #если у файла есть дата в названии файла, то переименуем (уменьшим на год)
            new_path = Path(root, new_name)
            os.rename(_path, new_path)
            photos_list.writelines(str(count) + " s:" + root + "\\" + file + " ==>"
                                       + old_datetime.strftime(DATETIME_STR_FORMAT) + " <++>"
                                       + new_datetime.strftime(DATETIME_STR_FORMAT) + " *** "
                                       + root + "\\" + new_name + '\n')


        else:
            photos_list.writelines(str(count) + " s:" + root + "\\" + file + " ==>:"
                                       + old_datetime.strftime(DATETIME_STR_FORMAT) + " <++>:"
                                       + new_datetime.strftime(DATETIME_STR_FORMAT) +  '\n')





print("all = ", count)
print("The end")