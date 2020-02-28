import os
import shutil
def find (name, path):
    results = []
    filename = name + '.rar'
    for root, dirs, files in os.walk(path):
        for x in files:
            if filename in x:
                results.append(os.path.join(root, name))
                shutil.move(x, 'testfolder')
            else:
                return os.path.join(root, name)
find(name = 'weapon', path = '/home/malachi/Desktop/projects/modorg')
