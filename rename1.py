import os
from os.path import join, getsize
import pathlib
from pathlib import Path
import time
import shutil



directory2 = '/mnt/hdd1/photos/photo_mix1'
path_list = Path(directory2, "_list.txt")
path_errors_list = Path(directory2, "_errors.txt")

photos_list = open(path_list, 'w')
errors_list = open(path_errors_list, 'w')
count = 0

for root, dirs, files in os.walk(directory):


    for file_ in files:

        file = file_.upper()
        count += 1
        #if count == 300:
        #    break
