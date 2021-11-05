from typing import Any

import os
from os.path import join, getsize
import pathlib
from pathlib import Path
import time
import shutil


#directory = '/mnt/hdd1/photos/фото_актуальное_это_заполнять'
#directory2 = "C:\\Users\\chery\OneDrive - Citrus College\Desktop\Новая папка\IMG_0913.JPG"
path_old = "C:\\Users\chery\OneDrive - Citrus College\Desktop\Новая папка\IMG_0913.JPG"
path_new = '2014-01-29 15-42-55.JPG'
hand_made = '2007-07-12 17-34-07'


count = 0
count_trash = 0

full_old = path_old
fn_old, file_extension_old = os.path.splitext(full_old)

#full_new = Path(directory2, path_new)
#fn_new, file_extension_new = os.path.splitext(full_new)

_time = time.gmtime(os.path.getmtime(full_old))
_time_c = time.gmtime(os.path.getctime(full_old))

print(_time)
print(_time_c)


time_new = ""


