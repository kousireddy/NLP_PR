import re
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Natural Language Processing (NLP) is a field of Artificial Intelligence that focuses on the interaction between computers and humans through language. NLP enables computers to understand, interpret, and generate human language. Many applications like chatbots, search engines, and recommendation systems use NLP techniques to improve user experience. As technology grows, NLP is becoming more powerful and widely used in industries."

#convert into lowercase
text = text.lower()

#Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

#remove extra spaces
text = re.sub(r'\s+',' ',text).strip()

#tokenize
tokens = word_tokenize(text)

#remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]

#count_frequency
word_counts = Counter(tokens)

print("Word Frequencies:")
print(word_counts)

print("\nTop 3 Most Frequent Words:")
print(word_counts.most_common(3))