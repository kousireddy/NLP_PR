import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer


def preprocess_text(text, use_stemming=False):
    #Convert to lowercase
    text = text.lower()

    #Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    #Remove numbers
    text = re.sub(r'\d+', '', text)

    #Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    #Tokenization
    tokens = word_tokenize(text)

    #Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    #Stemming OR Lemmatization
    if use_stemming:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(word) for word in tokens]
    else:
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word, pos='v') for word in tokens]

    return tokens


#Sample Text
sample_text = "Hello!!! I was running and studying NLP in 2026. It is AMAZING!!!"

print("Original Text:")
print(sample_text)

print("\nUsing Lemmatization:")
print(preprocess_text(sample_text, use_stemming=False))

print("\nUsing Stemming:")
print(preprocess_text(sample_text, use_stemming=True))