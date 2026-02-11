import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[^a-z0-9₹$.,:\n ]', '', text)
    return text.strip()