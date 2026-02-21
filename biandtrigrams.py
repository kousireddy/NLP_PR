from nltk.util import ngrams
from nltk.tokenize import word_tokenize

sentence = "I love natural language processing"

# Convert to lowercase
sentence = sentence.lower()

# Tokenize
tokens = word_tokenize(sentence)

# Generate bigrams
bigrams = list(ngrams(tokens, 2))

# Generate trigrams
trigrams = list(ngrams(tokens, 3))

print("Tokens:", tokens)
print("\nBigrams:", bigrams)
print("\nTrigrams:", trigrams)