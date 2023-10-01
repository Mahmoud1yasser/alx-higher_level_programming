#!/usr/bin/python3
def text_indentation(text):
    """ function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text: string to be printed

    Raises: TypeError if entered is not string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    to_prnt = text.replace('.', '.\n\n')
    to_prnt = to_prnt.replace('?', '?\n\n')
    to_prnt = to_prnt.replace(':', ':\n\n')
    prnt_final = to_prnt.split('\n')
    for line in range(len(prnt_final)):
        print("{}".format(prnt_final[line].strip()),
              end=("" if (line == (len(prnt_final) - 1)) else '\n'))
