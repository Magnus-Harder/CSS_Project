import re
from nltk.corpus import stopwords
from nltk import word_tokenize

def tokenize(text):
    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)

    # Exclude punctuation and numbers and set everything to lower case.
    text = word_tokenize(text)
    text = [w.lower() for w in text if w.isalpha()]

    # Exclude stopwords
    text = [w for w in text if not w.lower() in set(stopwords.words('english'))]

    # Save
    return text