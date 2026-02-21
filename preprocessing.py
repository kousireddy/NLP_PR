import nltk
from nltk.tokenize import word_tokenize
import string

text = "Hello!!! How are you???"
tokens = word_tokenize(text)

clean_tokens = [word for word in tokens if word not in string.punctuation]

print(clean_tokens)