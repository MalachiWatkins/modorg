import os
import shutil
import time
import copy
import sys
path_to_files = os.getcwd() + '/'
def anotherone(file_name, movefolderpath):
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if file_name in x:
                shutil.move(x, movefolderpath)
                time.sleep(.5)
            else:
                exit()
    return
def category(pathtofiles):
    file_tag = input("Enter an inital file tag to use:  ")
    exinput = input('Enter a file Extention to use like .rar:  ')
    folder_path = input('Enter the folder where you want the files to go: ')
    move_folder_path = path_to_files + folder_path
    filename = file_tag + exinput
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                time.sleep(.5)
                done = 'Successfully moved file or files' + ' to ' + move_folder_path
                print(done)
                anotherone(file_name = filename, movefolderpath = move_folder_path)

            else:
                print('Your file was not found')
                time.sleep(.5)
                moreinp = input('Would you like to use another tag (yes:no): ')
                if moreinp == 'yes':
                    category(pathtofiles = path_to_files)
                else:
                    exit()
                return os.path.join(root, file_tag)

category(pathtofiles = path_to_files)
