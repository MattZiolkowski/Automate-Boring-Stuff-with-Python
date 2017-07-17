#! python3

#This program copies .jpg files in the entire folder directory to a new location

import shutil
import os

newFolder = r'C:\Users\New\Folder\Location\'

def copyJPG(folder):
    for folder, subfolders, filenames in os.walk(folder):
        folder = os.chdir(folder)
        for filename in filenames:
            if not filename.endswith('.jpg'):
                continue
            print('Copying %s to %s...' % (filename, newFolder))
            shutil.copy(filename, newFolder)


copyJPG(r'C:\Users\Orginal\Folder\Location\To\Copy')
print('Done.')
