#!/bin/python3
# threadedDownloadIdioms.py - Downloads idioms from https://www.theidioms.com/list/page/

import requests
import os, bs4, threading  #, pickle
import re
from time import sleep
import random, time

os.makedirs('Idioms', exist_ok=True)  # store idioms in ./Idioms


def download(startPage, endPage):

    name=threading.current_thread().name
    print(f'Tread n°{name} active')
    
    for urlNumber in range(startPage, endPage):  # Download the page.
        pageLocalName = os.path.basename(str(urlNumber)+".html")
        pageLocalPath = os.path.join('Idioms', pageLocalName)

        print(f'Path: {pageLocalPath}, found: {os.path.exists(os.path.join("Idioms", pageLocalName))}')
        
        if os.path.exists(pageLocalPath):
            print(f'Tread n°{name}, parsing the local file.', end='')
            print(f"File {pageLocalPath} exists locally, using it")
            mFile = open(pageLocalPath,'rb')
            soup = bs4.BeautifulSoup(mFile, 'html.parser')
            #print(soup.prettify())
            
        else:
            r = random.randint(1,10)
            print(f'Tread n°{name}, sleeping for {r} sec')
            sleep(r)  # not overload the server
    
            print('Downloading page https://www.theidioms.com/list/page/%s/' % (urlNumber))
            res = requests.get('https://www.theidioms.com/list/page/%s/' % (urlNumber))
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            print(f'Writing file: {pageLocalName}')
            mFile = open(pageLocalPath,'wb')
            for chunk in res.iter_content(100000):
                mFile.write(chunk)
            mFile.close()
            #print(soup.prettify())

        #exit(1)

        # Find the idioms of the idiom page.
        idiomElemsDt = soup.find_all('dt')
        #print(idiomElemsDt)
        
        idiomElemsDd = soup.find_all('dd')
        #print(idiomElemsDd)

        if idiomElemsDt == [] or idiomElemsDd == []:
            print('Could not find idioms.')
        else:  # Write the idioms.
            pageLocalName = os.path.basename(f'{urlNumber:0>4}'+".txt")
            #print(f'Output file: {pageLocalName}')
            pageLocalPath = os.path.join('Idioms', pageLocalName)
            mFile = open(pageLocalPath, 'w', encoding='utf-8')
            # for a in idiomElemsDt:
            #     print(f'Anchor: {a}')
            #     myIdiom = a.getText().capitalize()
            #     print(f'Text: {myIdiom}')
            # print('-----')
            # for a in idiomElemsDd:
            #     print(f'Anchor: {a}')
            #     print(f'Text: {a.getText()}')
            #     #m = re.search(r'(?<=Meaning:)\w*(?<=Example:)\w*',a.getText())
            #     m = re.search(r'Meaning:(.*)Example:(.*\.)',a.getText())
            #     print('Regexp: ', m.group(), m.groups())
            #     myMeaning = m.group(1)
            #     myExample = m.group(2)
            #     print(f'{myMeaning=},\n{myExample=}')
            #print('-----')
            for i in range(len(idiomElemsDt)):
                #print(f'AnchorDt: {idiomElemsDt[i]}')
                #print(f'AnchorDd: {idiomElemsDd[i]}')
                myIdiom = idiomElemsDt[i].getText().capitalize()
                #print(f'myIdiom: {myIdiom}')
                #print('Text: ', idiomElemsDd[i].getText())
                m = re.search(r'.*Meaning:\s*(.*?)\.?Examples?:\s*[0-9]*\.*\s*(.*?)\.?\s*Read on(.*)',idiomElemsDd[i].getText())
                if m:
                    #print(m.groups())
                    if m.group(1):
                        myMeaning = m.group(1).lower()
                    else:
                        myMeaning = ''
                    if m.group(2):
                        myExample = m.group(2)
                    else:
                        myExample = ''
                    sentences = [s.capitalize() for s in myExample.split(". ")]
                    myExampleCapitalized = '. '.join(sentences)
                    #print(f'myMeaning: {myMeaning}\nmyExample: {myExample}')
                    s = myIdiom + ': ' + myMeaning + '. ' + myExampleCapitalized + '\n'
                    #print(f'{s}')
                else:
                    s = myIdiom + '\n'
                mFile.write(s)
                print('--')
                
            #print('-----')
            mFile.close()
            with open(pageLocalPath, 'r', encoding='utf-8') as mFile:
                contents = mFile.read()
            print(contents)


# Test
t_start = time.time()
#download(102,103)  # downloads page n°x


# Create and start the Thread objects.
b = False
if b:
    downloadThreads = []
    # a list of all the Thread objects
    for i in range(1, 147, 10):  # loops 14 times, creates 14 threads
        start = i
        end = i + 10  # deals with end-start page(s) at a time
        downloadThread = threading.Thread(target=download, name='T{0}'.format(i), args=(start, end))
        downloadThreads.append(downloadThread)
        downloadThread.start()


    # Wait for all threads to end.
    for downloadThread in downloadThreads:
        downloadThread.join()
t_end = time.time()
print(f'Done. Execution time: {t_end - t_start} sec')


# Merge the results

t_start = time.time()
p = pathlib.Path("./Idioms")  # pathlib.Path.cwd()
txt_files = p.glob("*.txt")
l = list(txt_files)
print("*.txt:", l)

if os.path.exists(p / 'idioms_all.txt'):
    print(f'Delete existing idioms_all.txt in {p}')
    os.unlink(p / 'idioms_all.txt')
    
print(f'Creating idioms_all.txt in {p}')

with open(p / 'idioms_all.txt','a', encoding='utf-8') as f0:
    print(f'File idioms_all.txt in {p} created')
    print(f'{l=}')
    for f in l:
        s = str(f)
        print(f'Dealing with file {s}')
        with open(f, 'r', encoding='utf-8') as mFile:
            print(f"Appending file {f} in {f0.name}")
            contents = mFile.read()
            #print(f'Content of file {f}: {contents}')
            f0.write(contents)


with open(p / 'idioms_all.txt', 'r', encoding='utf-8') as mFile:
    contents = mFile.read()
    #print(contents)

t_end = time.time()
print(f'Done. Execution time: {t_end - t_start} sec')
    
