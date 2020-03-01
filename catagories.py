import os
import shutil
import time
import copy
import sys
path_to_files = '/home/malachi/Desktop/projects/modorg'
move_folder_path = '/home/malachi/Desktop/projects/modorg/testfolder'
def anotherone(file_name):
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if file_name in x:
                shutil.move(x, move_folder_path)
                time.sleep(.5)
            else:
                exit()
    return
def category(pathtofiles, move_folder_path):
    file_tag = input("Enter an inital file tag to use:  ")
    exinput = input('Enter a file Extenrtion to use like .rar:  ')

    filename = file_tag + exinput
    for root, dirs, files in os.walk(path_to_files): # gets the path and uses os walk to cycle trough dirs
        for x in files:
            if filename in x: # checks if file name is there
                shutil.move(x, move_folder_path) # moves selected file to selected directory absolute path needed
                print('yes') #  progress bar
                time.sleep(.5) # pauses for x seconds befor running second function so everythins wrorks properly
                anotherone(file_name = filename)
            else:
                print(filename + '  was not found')
                time.sleep(.5)
                moreinp = input('Would you like to use another tag (yes:no): ')
                if moreinp == 'yes':
                    category(pathtofiles = path_to_files, move_folder_path = move_folder_path)
                else:
                    exit()
                return os.path.join(root, file_tag)
category(pathtofiles = path_to_files, move_folder_path = move_folder_path)
