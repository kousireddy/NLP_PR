import streamlit as st
import pickle
import string
from nltk.corpus import stopwords

# Load saved model
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

#UI
st.set_page_config(page_title="Sentiment Analyzer", page_icon="")

st.title("Sentiment Analyzer")

review = st.text_area("Enter a movie review:")

if st.button("Analyze"):
    cleaned = clean_text(review)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    if prediction == 1:
        st.success("Positive Review")
    else:
        st.error("Negative Review")