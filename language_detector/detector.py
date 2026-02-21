from langdetect import detect, DetectorFactory

# Make results consistent
DetectorFactory.seed = 0

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Could not detect language"