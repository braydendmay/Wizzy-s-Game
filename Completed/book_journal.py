import time
import os
import sys
clear = lambda: os.system('cls')

chpt = ''
pg = ''
note = ''
fileName = ''
combine = ''

def main():
    global chpt
    global pg
    global note
    global fileName
    print('----------------\nNew Note:')
    chpt = input('Chapter: ')
    pg = input('Page #: ')
    print('----------------')
    note = input('Type note here:\n').lower()
    clear()
    print('----------------')
    fileName = input('Enter file name: ')
    clear()
    print('Uploading Notes to file...')
    time.sleep(.7)
    clear()
    print('Uploading Notes to file..')
    time.sleep(.7)
    clear()
    print('Uploading Notes to file.')
    time.sleep(.7)
    clear()
    print('Uploading Notes to file..')
    time.sleep(.7)
    clear()
    print('Uploading Notes to file...')
    time.sleep(.7)
    clear()
    combine = (f'Chapter: {chpt} Page #: {pg} Note: {note}')
    with open(f'textFiles/{fileName}.txt', 'a') as destination:
        destination.write(combine + '\n')
        combine = ''
    with open('textFiles/notes.txt', 'a') as destination:
        destination.write(fileName + '\n')

def read_notes():
    fileName = input('Enter file name: ')
    clear()
    read_or_search = input('1.Search\n2.Read all\nEnter: ')
    if read_or_search == '1':
        clear()
        search_by = input('Search by: \n1.Chapter\n2.Page #\n3.Keyword\nEnter: ').lower()
        clear()
        if search_by == '1' or search_by == 'chapter':
            search_chpt = input('Chapter #: ')
            with open(f'textFiles/{fileName}.txt', 'r') as source:
                notebook = source.readlines()
            for lines in notebook:
                if lines.find(f'Chapter: {search_chpt} ') != -1:
                    print(lines)

        elif search_by == '2' or search_by == 'page #':
            search_pg = input('Page #: ')
            with open(f'textFiles/{fileName}.txt', 'r') as source:
                notebook = source.readlines()
            for lines in notebook:
                if lines.find(f'Page #: {search_pg} ') != -1:
                    print(lines)

        elif search_by == '3' or search_by == 'keyword':
            search_keyword = input('Keyword: ').lower()
            with open(f'textFiles/{fileName}.txt', 'r') as source:
                notebook = source.readlines()
            for lines in notebook:
                if lines.find(f'{search_keyword} ') != -1:
                    print(lines)

    elif read_or_search == '2':
        clear()
        print('✨NoteBook✨\n--------------------------------')
        with open(f'textFiles/{fileName}.txt', 'r') as source:
            notebook = source.readlines()
            for lines in notebook:
                print(lines.strip())
            
    cont = input('--------------------------------\nPress ENTER to continue: ')
    clear()

def show_note_files():
    with open('textFiles/notes.txt', 'r') as source:
        show_notes = source.readlines()
        for i in range(len(show_notes)):
            print(f'{i+1}.{show_notes[i]}')     
    cont = input('Press ENTER to continue: ')     
    clear()

run =True

while run == True:
    clear()
    add_or_read = input('1.Make new note\n2.Read notebook\n3.See note files\nEnter: ')
    if add_or_read == '1':
        clear()
        main()
    elif add_or_read == '2':
        clear()
        read_notes()
    elif add_or_read == '3':
        clear()
        show_note_files()