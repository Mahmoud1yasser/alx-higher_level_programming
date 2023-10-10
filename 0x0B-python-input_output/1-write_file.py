#!/usr/bin/python3
# 1-write_file.py
'''Write a function that writes a string to a text file (UTF8)
and returns the number of characters written'''


def write_file(filename="", text=""):
    '''function writes in a file with UTF8 formate
    Returns: number of charachters written'''
    with open(filename, 'r+', encoding='UTF-8') as f:
        return f.write(text)
