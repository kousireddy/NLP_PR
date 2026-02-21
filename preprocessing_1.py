import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#sample text
text = "Hello!!! I am Learning NLP in 2026. It's running"

print("Original Text: ",text)

#Lowercase
text = text.lower()
# print("lower case text: ",text)

#remove punctuation
text=re.sub(r'[^\w\s]','',text)

#tokenization
tokens = word_tokenize(text)

# print("after word tokenization:",tokens)

#remove stopwords
stop_words=set(stopwords.words('english'))
# print("stop_words:",stop_words)

tokens=[word for word in tokens if word not in stop_words]

#lemmatization
lemmatizer = WordNetLemmatizer()
output_tokens=[lemmatizer.lemmatize(word,pos='v') for word in tokens]

print("Final processed tokens: ",output_tokens)


