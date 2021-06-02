#!/bin/python3
# threadedDownloadIdioms.py - Downloads idioms from https://www.theidioms.com/list/page/

import requests
import os, bs4, threading  #, pickle
import re

os.makedirs('Idioms', exist_ok=True)  # store idioms in ./Idioms


def download(startPage, endPage):
    for urlNumber in range(startPage, endPage):  # Download the page.
        pageLocalName = os.path.basename(str(urlNumber)+".html")
        pageLocalPath = os.path.join('Idioms', pageLocalName)

        print(f'Path: {pageLocalPath}, found: {os.path.exists(os.path.join("Idioms", pageLocalName))}')
        
        if os.path.exists(pageLocalPath):
            print(f"File {pageLocalPath} exists locally, using it")
            mFile = open(pageLocalPath,'rb')
            soup = bs4.BeautifulSoup(mFile, 'html.parser')
            #print(soup.prettify())
            
        else:
            break
            print('Downloading page https://www.theidioms.com/list/page/%s/' % (urlNumber))
            res = requests.get('https://www.theidioms.com/list/page/%s/' % (urlNumber))
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            print(f'Writing file: {pageLocalName}')
            mFile = open(pageLocalPath,'wb')
            for chunk in res.iter_content(100000):
                mFile.write(chunk)
            mFile.close()
            print(soup.prettify())

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
            print(f'Output file: {pageLocalName}')
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
            print('-----')
            for i in range(len(idiomElemsDt)):
                #print(f'Anchor: {idiomElemsDt[i]}')
                myIdiom = idiomElemsDt[i].getText().capitalize()
                m = re.search(r'Meaning:(.*)Example:(.*\.)',idiomElemsDd[i].getText())
                myMeaning = m.group(1)
                myExample = m.group(2)
                #print(f'{myIdiom=}')
                #print(f'{myMeaning=},\n{myExample=}')
                s = myIdiom + ':' + myMeaning + '.' + myExample + '\n'
                print(f'{s}')
                mFile.write(s)
                print('--')
                
            print('-----')
            mFile.close()
            with open(pageLocalPath, 'r', encoding='utf-8') as mFile:
                contents = mFile.read()
            print(contents)

            
# TODO: Create and start the Thread objects.
# TODO: Wait for all threads to end.

download(1,2)
