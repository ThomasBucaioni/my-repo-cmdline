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
            new_proxy_file = open('_proxy_new', 'w')
            filelines = current_proxy_file.readlines()
            indent8line = False
            indent12line = False
            indocstring = False
            for line in filelines:
                logging.debug(line)
                newline = line
                if line != '\n':
                    logging.debug('Line not empty: >>>' + line + '<<<')
                    if '"""' == line.lstrip()[0:3]:
                        indocstring = not indocstring
                        logging.debug(indocstring)
                        if indocstring:
                            logging.debug('In docstrings')
                            indent8line = False
                            indent12line = False
                        else:
                            logging.debug('Out docstrings')
                            indocstring = False
                    if indocstring:
                        if ':param' == line.lstrip()[0:6] or \
                           ':retur' == line.lstrip()[0:6] or \
                           ':raise' == line.lstrip()[0:6]:
                            print('Ok:', line[0:20])
                            indent8line = True
                            indent12line = False
                            newline = ' ' * 8 + line.lstrip()
                        elif indent8line == True:
                            logging.debug('line to debug: >>>' + line + '<<<')
                            if line.lstrip()[0] == '*':
                                indent12line = True
                                newline = ' ' * 12 + line.lstrip()
                            elif indent12line == True:
                                newline = ' ' * 16 + line.lstrip()
                            else:
                                newline = ' ' * 12 + line.lstrip()
                        elif '"""' == line.lstrip()[0:3]:
                            indent8line = False
                            indent12line = False
                            newline = ' ' * 8 + line.lstrip()
                print(newline[0:len(newline)])
                new_proxy_file.write(newline)
                #input("Press Enter to continue...")
            new_proxy_file.close()
            current_proxy_file.close()
print('')

logging.debug('End cleaning docstrings')
