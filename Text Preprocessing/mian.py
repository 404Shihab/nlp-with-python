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


import string, time

# Get all punctuation characters from the string module
exclude = string.punctuation


def remove_punc(text):
    for char in exclude:
        text = text.replace(char, '')
    return text



text = """
Shihab. Uddin. Bhuiyan!! hi, how are you?
Hello! World! Bye, Mars
"""


# Record the starting time
start = time.time()

# Remove punctuation and print the cleaned text
print(remove_punc(text))

# Calculate the execution time
time1 = time.time() - start

# Print the execution time
print(time1)


# --- Faster method ---

# Remove punctuation using translate() and maketrans()
def remove_punc2(text):
    return text.translate(str.maketrans('', '', exclude))



start = time.time()


print(remove_punc2(text))
time2 = time.time() - start
print(time2)


# Compare the execution time of both methods
print(time1 / time2)

#---------- compare with large data set ----------------- 
large_text = text * 100000

start = time.time()
remove_punc(large_text)
time1 = time.time() - start

start = time.time()
remove_punc2(large_text)
time2 = time.time() - start

print("Method 1:", time1)
print("Method 2:", time2)
print("Speed ratio:", time1 / time2)


# -- 

df2 = pd.read_csv("Text Preprocessing/labeled_data.csv")

# print(df2)


print(df2['tweet'].apply(remove_punc2))