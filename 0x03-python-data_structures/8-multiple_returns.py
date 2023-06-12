#!/usr/bin/python3

'''
 multiple_returns-returns tuple with length of string and its first character.
 @sentence:sentence input
 Return:length of string, first character
 '''


def multiple_returns(sentence):
    if sentence[0] is None:
        return len(sentence), None
    else:
        return len(sentence), sentence[0]
