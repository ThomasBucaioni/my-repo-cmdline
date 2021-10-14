from pathlib import Path
import shutil, os
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start cleaning docstrings')

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
                #logging.info(line)
                #logging.info(line.lstrip()[0:6])
                if ':param' == line.lstrip()[0:6]:
                    print('Ok:', line)
print('')

logging.debug('End cleaning docstrings')
