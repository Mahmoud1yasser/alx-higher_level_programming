#!/usr/bin/python3
# 2-append_write.py
'''Append to a file '''


def append_write(filename="", text=""):
    '''unction that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Returns: number of characters printed
    '''
    with open(filename, 'a', encoding='UTF-8') as f:
        count = f.write(text)
        return count
