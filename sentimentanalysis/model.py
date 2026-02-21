import pandas as pd
import string
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords

# Sample Dataset
data = {
    "review": [
        "I love this product",
        "This is amazing",
        "Very happy with the service",
        "I hate this item",
        "Worst experience ever",
        "Very bad quality"
    ],
    "sentiment": [1, 1, 1, 0, 0, 0]  # 1=Positive, 0=Negative
}

df = pd.DataFrame(data)

#Preprocessing
stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df["review"] = df["review"].apply(clean_text)

#TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["review"])
y = df["sentiment"]

#Model
model = LogisticRegression()
model.fit(X, y)

#Save Model
pickle.dump(model, open("sentiment_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved successfully!")