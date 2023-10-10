#!/usr/bin/python3
'''Python Function that reads a file and prints to stdout'''


def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
