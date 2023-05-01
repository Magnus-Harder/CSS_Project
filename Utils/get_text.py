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


def text_page(char : list, page : list) -> list:
    text = []
    for i,line in enumerate(page):
        if any(alias in line for alias in char):
            if i == 0:
                try:
                    text.append([page[i], page[i+1]])
                except:
                    text.append([page[i]])
            elif i == len(page)-1:
                text.append([page[i-1], page[i]])
            else:
                text.append([page[i-1], page[i], page[i+1]])
            
    return text

def text_chapter(char : list, chapter : list) -> list:
    text = []
    for page in chapter:
        text.append(text_page(char, page))
    return text

def tokenize_text(text : list) -> str:
    text_tokenized = []

    for page in text:
        for finding in page:
            for sentence in finding:
                text_tokenized.extend(tokenize(sentence))
    return text_tokenized

def text_book(char : list, book_text : dict) -> dict:
    text = {}
    for chapnr,chapter in book_text.items():
        text[chapnr] = tokenize_text(text_chapter(char, chapter))
    return text

# %%
