#!/usr/bin/python3
# 6-load_from_json_file.py
'''Create object from a JSON file '''


def load_from_json_file(filename):
    '''function that creates an Object from a “JSON file'''
    import json
    with open(filename, 'r') as f:
        return json.loads(f.read())
