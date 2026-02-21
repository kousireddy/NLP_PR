import pandas as pd
import string
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords

#Sample Dataset
data = {
    "message": [
        "Win money now",
        "Congratulations you won a lottery",
        "Call this number to claim prize",
        "Hey how are you",
        "Let's meet tomorrow",
        "Are you coming to class?"
    ],
    "label": ["spam", "spam", "spam", "ham", "ham", "ham"]
}

df = pd.DataFrame(data)

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df["message"] = df["message"].apply(clean_text)

#TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["message"])
y = df["label"]

#Model
model = MultinomialNB()
model.fit(X, y)

#Save Model
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Spam model trained and saved!")