import exifread
import os
from os.path import join, getsize
import pathlib
from pathlib import Path
import time
import shutil

directory = 'H:\\фото_актуальное_это_заполнять'
directory2 = 'H:\\фото_актуальное_это_заполнять'
path_list = Path(directory2, "_list.txt")
path_errors_list = Path(directory2, "_errors.txt")

#photos_list = open(path_list, 'w')
#errors_list = open(path_errors_list, 'w')
count = 0
count_trash = 0




path_name = 'H:\фото_актуальное_это_заполнять\\1_ЗАПИСАННЫЕ\\2007_05_01\Изображение 095.JPG'
f = open(path_name, 'rb')
tags = exifread.process_file(f)

print(tags)
print(tags['EXIF DateTimeDigitized'])
print(tags['EXIF DateTimeOriginal'])

