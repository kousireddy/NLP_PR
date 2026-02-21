import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ---------- Preprocessing ----------
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word, pos='v') for word in tokens]

    return tokens


# ---------- Response Generator ----------
def generate_response(user_input):
    tokens = preprocess(user_input)

    if "hi" in tokens or "hello" in tokens:
        return "Hello! How can I help you?"

    elif "morning" in tokens:
        return "Good morning! Hope you have a productive day!"

    elif "afternoon" in tokens:
        return "Good afternoon! How is your day going?"

    elif "evening" in tokens:
        return "Good evening! How can I assist you?"

    elif "how" in tokens and "are" in tokens:
        return "I'm just a chatbot, but I'm functioning perfectly!"

    elif "who" in tokens and "created" in tokens:
        return "I was created by a developer using Python and NLP."

    elif "what" in tokens and "can" in tokens and "do" in tokens:
        return "I can answer simple questions, greet you, and chat using NLP preprocessing."

    elif "python" in tokens:
        return "Python is a powerful programming language used for AI, ML, and web development."

    elif "streamlit" in tokens:
        return "Streamlit is a Python library used to build interactive web apps easily."

    elif "nlp" in tokens:
        return "NLP stands for Natural Language Processing. It helps machines understand human language."

    elif "machine" in tokens and "learning" in tokens:
        return "Machine Learning allows computers to learn patterns from data."

    elif "joke" in tokens:
        return "Why did the computer go to the doctor? Because it caught a virus!"

    elif "time" in tokens:
        import datetime
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

    elif "date" in tokens:
        import datetime
        return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}"

    elif "weather" in tokens:
        return "I can't check live weather yet, but it's always a good day to code!"

    elif "project" in tokens:
        return "You can build projects like Chatbots, Sentiment Analysis, or ML prediction apps."

    elif "internship" in tokens:
        return "Internships help you gain real-world experience and improve your skills."

    elif "database" in tokens:
        return "Databases store structured data. Examples include MySQL and PostgreSQL."

    elif "django" in tokens:
        return "Django is a powerful Python web framework used to build secure applications."

    elif "flask" in tokens:
        return "Flask is a lightweight Python framework for building web APIs."

    elif "thanks" in tokens:
        return "Happy to help!"

    elif "bye" in tokens or "goodbye" in tokens:
        return "See you soon!"

    else:
        return "Sorry, I didn't understand that."