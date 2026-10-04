import pandas as pd
import re



df = pd.read_csv("Text Preprocessing/IMDB Dataset.csv")

# print(df.head())

# print(df)
print(df.shape) # (50000, 2)

# 1 ---lowercasing---
print(df['review'].str.lower())

# 2 -- remove html tags --- 

def remove_html_tags(text):
    pattern = compile()