---
created: 2025-01-08T09:16:43-08:00
modified: 2025-01-08T09:16:56-08:00
---

# natural_language_processing.py

import nltk
from nltk.tokenize import word_tokenize

def tokenize_text(text):# natural_language_processing.py
import nltk
from nltk.tokenize import word_tokenize

def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens

def remove_stopwords(tokens):
    stopwords = nltk.corpus.stopwords.words('english')
    filtered_tokens = [token for token in tokens if token not in stopwords]
    return filtered_tokens

def lemmatize_tokens(tokens):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens
