#!/usr/bin/python3
"""This is text indentation module"""


def text_indentation(text):
    """
    Splits a text into lines along '?', ':', '.', followed by 2 new lines.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char != ' ':
                flag = 1
        if flag == 1:
            if char in ['?', '.', ':']:
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
