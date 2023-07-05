#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    punctuation = ["?", ".", ":"]
    start_new_line = True

    for char in text:
        if start_new_line and char == ' ':
            continue
        if char == ' ' and result[-1] == ' ':
            continue

        result += char
        if char in punctuation:
            result += '\n\n'
            start_new_line = True
        else:
            start_new_line = False
    print(result, end='')
