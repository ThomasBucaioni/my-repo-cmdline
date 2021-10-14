from pathlib import Path
import shutil, os

for folderName, subfolders, filenames in os.walk('.'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        if filename == '_proxy.py':
            print('FILE INSIDE ' + folderName + ': '+ filename)
            current_proxy_file = open(filename, 'r')
            filelines = current_proxy_file.readlines()
            for line in filelines:
                #print(line)
                #print(line.lstrip()[0:6])
                if ':param' == line.lstrip()[0:6]:
                    print('Ok:', line)
print('')
