#!/usr/bin/python3
# 100-append_after.py
'''Search and update '''

def append_after(filename="", search_string="", new_string=""):
    '''function that inserts a line of text to a file,
    after each line containing a specific string'''
    txt = ""
    with open(filename, 'r') as f:
        f_line = f.readline()
        while f_line != "":
            txt += f_line
            if search_string in f_line:
                txt += new_string
            f_line = f.readline()
    with open(filename, 'w') as f:
        f.write(txt)
