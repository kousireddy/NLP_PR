from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()


text = "The boys are playing and running happily"

tokens = word_tokenize(text.lower())

stemmed_words = [stemmer.stem(word) for word in tokens]

print("Original Tokens:", tokens)
print("Stemmed Tokens:", stemmed_words)