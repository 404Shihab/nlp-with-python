import pandas as pd
import re



df = pd.read_csv("Text Preprocessing/IMDB Dataset.csv")

# print(df.head())

# print(df)
# print(df.shape) # (50000, 2)

# 1 ---lowercasing---
# print(df['review'].str.lower())

# 2 -- remove html tags --- 
text = """
<html>
    <body>
        <h1>Welcome to NLP</h1>
        <p>NLP stands for Natural Language Processing.</p>
        <p>Python is very useful for <b>text processing</b>.</p>
        <a href="https://example.com">Learn More</a>
    </body>
</html>
"""

def remove_html_tags(text):
    pattern = re.compile(r'<.*?>')
    return pattern.sub('', text)

# print(remove_html_tags(text))

# print(df['review'].apply(remove_html_tags))

# print(remove_html_tags(df['review'][3]))




# 3 ---- remove url ----




def remove_url(text):
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub('', text)




text1 = """
Welcome to my NLP project.

Visit https://www.google.com for more information.
You can also check http://example.com/page for details.

My portfolio is available at https://github.com/404Shihab.
For tutorials, visit www.example.com/tutorials.

Thank you!
"""

# print(remove_url(text1))


# 4 ---- remove punctuation ----


