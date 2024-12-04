# %%
# %pip install pandas numpy matplotlib
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
# %%
# 파일에서 중복되지 않은 단어의 개수 찾기
def find_unique_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        txt = file.read()
        txt = txt.replace("'s", '')

    txt = txt.replace('\n', ' ')
    words = re.findall(r'\b\w+\b', txt.lower())
    unique_words = set(words)
    return unique_words, len(unique_words)

words, words_len = find_unique_words('proverb.txt')

print(words)
print(words_len)
# %%
def process(w):
    output = " "
    for ch in w:
        if ch.isalpha():
            output += ch
    return output

words = set()
fname = 'proverb.txt'
file = open(fname, 'r', encoding='utf-8')

for line in file:
    line = line.strip()
    line = line.lower()
    words_list = line.split(' ')
    for word in words_list:
        words.add(process(word))

print(words)
print(len(words))
# %%
