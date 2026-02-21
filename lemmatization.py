import nltk
from nltk.stem import WordNetLemmatizer

words = ["running", "eating", "studies", "better"]

lemmatizer = WordNetLemmatizer()
for word in words:
    print("Noun:", lemmatizer.lemmatize(word))
    print("Verb:", lemmatizer.lemmatize(word, pos='v'))
    print()