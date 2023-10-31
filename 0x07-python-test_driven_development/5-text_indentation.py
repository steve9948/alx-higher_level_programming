#!/usr/bin/python3
"""
Function that prints a text with 2 new lines
after each of these characters: ., ? and : .

"""


def text_indentation(text):
    """
    Checks if text is astring,else throws an error.

    """
     if not isinstance(text, str):
        raise TypeError('text must be a string')
    if text == "":
        print('')
        return
    if text is None:
        raise EOFError('you must enter text to use the function')
    for ch in ['.', '?', ':']:
        if ch in text:
            text = text.replace(ch, '\n\n')
    print(text)
