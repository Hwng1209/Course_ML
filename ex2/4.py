
"""
# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
"""

import numpy as np
import string 

with open('D:\ML\ex2\story.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

text = " ".join(lines)
translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator)

words = np.array(text.split())

list_words, word_count = np.unique(words, return_counts=True)

mapping = np.array((list_words, word_count)).T

sort = np.flip(mapping[np.argsort(mapping[:, 1])])

for i in range(100):
    print(f"{sort[i][0]}: {sort[i][1]}")
