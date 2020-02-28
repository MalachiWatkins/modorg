import os
import shutil
def find (name, path):
    results = []
    for root, dirs, files in os.walk(path):
        for name in files:
            print('yes')
            if path.endswith(name):
                results.append(os.path.join(root, name))
                print('yes')
                shutil.move(name, 'testfolder')
        else:
            print('no')
            return os.path.join(root, name)
find(name = 'abc12', path = '/home/malachi/Desktop/projects/modorg')
