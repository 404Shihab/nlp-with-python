import pandas as pd

df = pd.read_csv("Text Preprocessing\\Chat word treatment\\words.csv")

chat_words = dict(zip(df["Word"], df["Meaning"]))

# print(df)

def chat_conversion(text):
    new_text = []

    for w in text.split():
        if w.upper() in chat_words:
            new_text.append(chat_words[w.upper()])
        else:
            new_text.append(w)

    return " ".join(new_text)


text = input("Enter your text: ")

print(chat_conversion(text))