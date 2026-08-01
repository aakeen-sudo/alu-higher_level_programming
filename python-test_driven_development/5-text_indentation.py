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
    length = len(stripped)
    i = 0

    while i < length:
        char = stripped[i]
        if char == " " and i > 0 and stripped[i - 1] in ".?:":
            i += 1
            continue
        print(char, end="")
        if char in ".?:":
            print("\n")
        i += 1