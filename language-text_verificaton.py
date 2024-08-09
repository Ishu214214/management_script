"""
English: Basic Latin characters are in the range \u0000 to \u007F.
Hindi: Devanagari script characters are in the range \u0900 to \u097F.
Spanish: Basic Latin characters, including accented letters, are in the range \u0000 to \u007F
"""

import re

def contains_chinese(text):
    # Regular expression pattern to match Chinese characters
    pattern = re.compile(r'[\u4e00-\u9fff]')  # Unicode range for Chinese characters
    # Search for the pattern in the text
    match = pattern.search(text)
    return match is not None

text = "你好吗？"
chines_test = contains_chinese(text)
print(chines_test)


def english_chinese(text):

    pattern = re.compile(r'[\u0000 -\u007F]')
    match = pattern.search(text)
    return match is not None

english_test = "ishu kumar "
english_test = english_chinese(english_test)
print(english_test)

