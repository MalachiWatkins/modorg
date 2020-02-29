import os
import shutil
import time
def category1(file_tag, file_extention, path_to_files, move_folder_path):
    # adds file extention to file name
    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files): # gets the path and uses os walk to cycle trough dirs
        for x in files:
            if filename in x: # checks if file name is there
                shutil.move(x, move_folder_path) # moves selected file to selected directory absolute path needed
                print('[#              ]') #  progress bar
                time.sleep(.5) # pauses for x seconds befor running second function so everythins wrorks properly
            else:
                return os.path.join(root, file_tag)
def category2(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[##             ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category3(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[###            ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category4(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[####           ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category5(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[#####          ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category6(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[######         ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category7(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[#######        ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category8(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[########       ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category9(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[#########      ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category10(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[##########     ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category11(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[###########    ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category12(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[############   ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category13(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[#############  ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category14(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[############## ]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
def category15(file_tag, file_extention, path_to_files, move_folder_path):

    filename = file_tag + file_extention
    for root, dirs, files in os.walk(path_to_files):
        for x in files:
            if filename in x:
                shutil.move(x, move_folder_path)
                print('[###############]')
                time.sleep(.5)
            else:
                return os.path.join(root, file_tag)
