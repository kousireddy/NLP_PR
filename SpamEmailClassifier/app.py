import streamlit as st
import pickle
import string
from nltk.corpus import stopwords

# Load model
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

#UI
st.set_page_config(page_title="Spam Classifier", page_icon="")

st.title("SMS Spam Classifier")

message = st.text_area("Enter SMS message:")

if st.button("Check"):
    cleaned = clean_text(message)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    if prediction == "spam":
        st.error("This message is SPAM")
    else:
        st.success("This message is NOT SPAM")