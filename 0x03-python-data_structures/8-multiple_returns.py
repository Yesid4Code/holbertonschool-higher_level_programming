#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        first_letter = None
    else:
        first_letter = sentence[0]
    return leng, first_letter
