# Enter your code here. Read input from STDIN. Print output to STDOUT

import requests
import re
from collections import Counter

# TEST
text = requests.get('http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt')
stop_words = requests.get(
    "https://gist.githubusercontent.com/sebleier/554280/raw/7e0e4a1ce04c2bb7bd41089c9821dbcf6d0c786c/NLTK's%2520list%2520of%2520english%2520stopwords")
stop_words_dict = {word.lower(): 1 for word in stop_words.text.split()}

text = text.text.split('\n')[244:]


def clean(word):
    word = word.replace("'", "")
    word = [c for c in word if c.isalpha()]
    return ''.join(word)


# split the text and convert to lower and skip stop_word
all_words = [clean(word.lower()) for line in text for word in line.split() if word.lower() not in stop_words_dict]
print(all_words)
top_5 = Counter(all_words).most_common(5)

for j in top_5:
    print(j[0])
