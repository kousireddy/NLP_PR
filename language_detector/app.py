import streamlit as st
from detector import detect_language

st.set_page_config(page_title="Language Detector", page_icon="")

st.title("Language Detection App")

text = st.text_area("Enter text:")

if st.button("Detect Language"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        result = detect_language(text)

        # Convert short codes to full names
        language_map = {
            "en": "English",
            "hi": "Hindi",
            "fr": "French",
            "de": "German",
            "es": "Spanish",
            "it": "Italian",
            "pt": "Portuguese",
            "ru": "Russian",
            "zh-cn": "Chinese",
            "ja": "Japanese",
            "te": "Telugu",
            "ta": "Tamil"
        }

        full_name = language_map.get(result, result)

        st.success(f"Detected Language: {full_name}")