from nltk.stem import PorterStemmer

#stemmer object
stemmer = PorterStemmer()

# Example words
words = ["running", "studies", "playing", "happiness", "easily"]

print("Original -> stemmed")
print("--------------------")

for word in words:
    print(word,"->",stemmer.stem(word))
