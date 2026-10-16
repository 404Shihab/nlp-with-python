
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

def remove_stopwords(text):
    new_text = []
    stop_words = stopwords.words('english')

    for word in text.split():
        if word not in stop_words:
            new_text.append(word)

    return " ".join(new_text)


text = "This is a simple example of removing stop words from text."
print(remove_stopwords(text))