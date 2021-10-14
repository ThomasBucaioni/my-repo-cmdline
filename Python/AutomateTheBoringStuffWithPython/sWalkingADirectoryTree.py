#!/bin/python3
import os
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
for folderName, subfolders, filenames in os.walk('.'):
    s = 'The current folder is ' + folderName
    print(s)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')

from pathlib import Path
p = Path(r'./')
print(p)
p.glob('*')
print(list(p.glob('*')))
print(list(p.glob('*.txt')))
    
