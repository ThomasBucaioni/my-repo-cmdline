from pathlib import Path
sonnetFile = open(Path.cwd() / 'sonnet29.txt')
print(sonnetFile.readlines())

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)
# <class 'shelve.DbfilenameShelf'>
print('Variable "cats" in mydata is:', shelfFile['cats'])
# ['Zophie', 'Pooka', 'Simon']
print(list(shelfFile.keys()))
#['cats']
print(list(shelfFile.values()))
#[['Zophie', 'Pooka', 'Simon']]
shelfFile.close()

import shutil, os
p = Path.cwd()
shutil.copy(p / 'bacon.txt', p / 'eggs.txt')
#shutil.move('bacon.txt', 'eggs.txt')

# Permanently Deleting Files and Folders
for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename)
    print(filename)

# Safe Deletes with the send2trash Module: `pip install --user send2trash`
import send2trash
baconFile = open('bacon.txt', 'a')
# creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')
