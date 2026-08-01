#!/usr/bin/python3
"""
Module 5-text_indentation

Defines a function that prints a text with 2 new lines
after each ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    stripped = text.strip()
    line = ""
    i = 0
    length = len(stripped)

    while i < length:
        char = stripped[i]
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
            i += 1
            while i < length and stripped[i] == " ":
                i += 1
            continue
        i += 1

    if line.strip():
        print(line.strip())