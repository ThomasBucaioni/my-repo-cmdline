from pathlib import Path
import shutil, os
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.DEBUG)

logging.debug('Start cleaning docstrings')

for folderName, subfolders, filenames in os.walk('/home/tbucaioni/homeopenstack/cloud/.'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        if filename[0] == '_' and filename[1] != '_':
            print('FILE INSIDE ' + folderName + ': '+ filename)
            logging.info('Cwd: ' + str(Path.cwd()))
            mypath = Path(os.path.abspath(folderName))
            logging.info('Path to the file: ' + str(mypath))
            current_proxy_file = open(mypath / filename, 'r')
            new_proxy_file = open(mypath / (filename + '_new.py'), 'w')
            filelines = current_proxy_file.readlines()
            indent8line = False
            indent12line = False
            indocstring = False
            for line in filelines:
                logging.debug(line)
                newline = line
                stripped = line.lstrip()
                logging.debug('Nl org:' + newline)
                if line != '\n':
                    logging.debug('Line not empty: >>>' + line.replace('\n', ' ') + '<<<')
                    if '"""' in line:
                        indocstring = not indocstring
                        logging.debug("Inside a docstring: " + str(indocstring))
                        if indocstring:
                            logging.debug('In docstrings')
                            indent8line = False
                            indent12line = False
                            leadingspaces = len(line) - len(stripped)
                        else:
                            logging.debug('Out docstrings')
                            indocstring = False
                    if indocstring:
                        if ':param' == stripped[0:6] or \
                           ':retur' == stripped[0:6] or \
                           ':rtype' == stripped[0:6] or \
                           ':attrs' == stripped[0:6] or \
                           ':type ' == stripped[0:6] or \
                           ':raise' == stripped[0:6]:
                            logging.debug('Item: --- ' + stripped[0:20] + ' ---')
                            indent8line = True
                            indent12line = False
                            newline = ' ' * leadingspaces + stripped
                            logging.debug('Nl ind8 :' + newline)
                        elif indent8line == True:
                            logging.debug('line to debug: >>>' + line + '<<<')
                            if stripped[0] == '*':
                                indent12line = True
                                newline = ' ' * (leadingspaces + 4) + stripped
                                logging.debug('Nl ind12 :' + newline)
                            elif indent12line == True:
                                newline = ' ' * (leadingspaces + 6) + stripped
                                logging.debug('Nl ind14 :' + newline)
                            else:
                                newline = ' ' * (leadingspaces + 4) + stripped
                                logging.debug('Nl ind12 :' + newline)
                        elif '"""' in stripped:
                            indent8line = False
                            indent12line = False
                            newline = ' ' * leadingspaces + stripped
                            logging.debug('Nl ind8 :' + newline[0:len(newline)])
                logging.debug('Nl wr:' + newline)
                new_proxy_file.write(newline)
#                input("Press Enter to continue...")
            new_proxy_file.close()
            current_proxy_file.close()
print('')

logging.debug('End cleaning docstrings')