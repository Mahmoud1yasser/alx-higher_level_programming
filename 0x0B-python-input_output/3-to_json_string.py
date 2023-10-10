#!/usr/bin/python3
# 3-to_json_string.py
'''To JSON string '''


def to_json_string(my_obj):
    '''function that returns the JSON representation of an object (string)'''
    import json
    return json.dumps(my_obj)
