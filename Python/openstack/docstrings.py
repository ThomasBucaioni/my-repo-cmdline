from pathlib import Path
import shutil, os
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.DEBUG)

logging.debug('Start cleaning docstrings')

for folderName, subfolders, filenames in os.walk('.'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        if filename == '_proxy.py':
            print('FILE INSIDE ' + folderName + ': '+ filename)
            logging.info('Cwd: ' + str(Path.cwd()))
            mypath = Path(os.path.abspath(folderName))
            logging.info('Path to the file: ' + str(mypath))
            current_proxy_file = open(mypath / filename, 'r')
            new_proxy_file = open(mypath / '_proxy_new.py', 'w')
            filelines = current_proxy_file.readlines()
            indent8line = False
            indent12line = False
            indocstring = False
            for line in filelines:
                logging.debug(line)
                newline = line
                if line != '\n':
                    logging.debug('Line not empty: >>>' + line.replace('\n', ' ') + '<<<')
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
                           ':rtype' == line.lstrip()[0:6] or \
                           ':attrs' == line.lstrip()[0:6] or \
                           ':type ' == line.lstrip()[0:6] or \
                           ':raise' == line.lstrip()[0:6]:
                            logging.debug('Ok:' + line[0:20])
                            indent8line = True
                            indent12line = False
                            newline = ' ' * 8 + line.lstrip()
                        elif indent8line == True:
                            logging.debug('line to debug: >>>' + line + '<<<')
                            if line.lstrip()[0] == '*':
                                indent12line = True
                                newline = ' ' * 12 + line.lstrip()
                            elif indent12line == True:
                                newline = ' ' * 14 + line.lstrip()
                            else:
                                newline = ' ' * 12 + line.lstrip()
                        elif '"""' == line.lstrip()[0:3]:
                            indent8line = False
                            indent12line = False
                            newline = ' ' * 8 + line.lstrip()
                logging.debug('Nw:' + newline[0:len(newline)])
                new_proxy_file.write(newline)
                #input("Press Enter to continue...")
            new_proxy_file.close()
            current_proxy_file.close()
print('')

logging.debug('End cleaning docstrings')
