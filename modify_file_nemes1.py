import os
from pathlib import Path

directory = 'I:\\dst'
count = 0

path_list = Path(directory, "_change_list.txt")
photos_list = open(path_list, 'w')
path_errors_list = Path(directory, "_change_errors.txt")
errors_list = open(path_errors_list, 'w')

for root, dirs, files in os.walk(directory):
    for file in files:

        count += 1

        old_name = file
        new_name = file[0:19].replace('_', '-') + file[19:]
        print(file + ' ' + new_name)

        old_path = Path(root, old_name)
        new_path = Path(root, new_name)



        try:
            os.rename(old_path, new_path)
            photos_list.writelines(str(count) + " s:" + root + '\\' + old_name + " ===>:" + new_name + '\n')
        except:
            errors_list.writelines(str(count) + "err s:" + root + '\\' + old_name + " ===>:" + new_name + '\n')



print(count)