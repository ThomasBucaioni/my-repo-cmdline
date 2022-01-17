from pathlib import Path
import shutil, os
import logging
import re
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.DEBUG)

logging.debug('Start cleaning docstrings')

for folderName, subfolders, filenames in os.walk('/home/tbucaioni/homeopenstack/cloud'):
    logging.info('The current folder is ' + folderName)
    for subfolder in subfolders:
        logging.info('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        if filename[0] == '_' and filename[1] != '_':
            logging.info('FILE INSIDE ' + folderName + ': '+ filename)
            logging.info('Cwd: ' + str(Path.cwd()))
            mypath = Path(os.path.abspath(folderName))
            logging.info('Path to the file: ' + str(mypath))
            current_proxy_file = open(mypath / filename, 'r')
#            new_proxy_file = open(mypath / (filename + '_new.py'), 'w')
            filelines = current_proxy_file.readlines()
            indent8line = False
            indent12line = False
            indocstring = False
            linecount = 0
            for line in filelines:
                logging.debug(line)
                linecount += 1
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
                        m1 = re.search(':class:\s*`[^`]+\n', line)
                        m2 = re.search(':class:\s+`.*`?', line)
                        if m1:
                            logging.info(f"Line {linecount}, m1: " + m1.group(0))
                        if m2:
                            logging.info(f"Line {linecount}, m2: " + m2.group(0))
#                input("Press Enter to continue...")
#            new_proxy_file.close()
            current_proxy_file.close()
print('')

logging.debug('End tracking broken classes in docstrings')
