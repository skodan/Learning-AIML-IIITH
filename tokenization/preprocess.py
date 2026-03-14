import pandas as pd
import re


# create function to preprocess text
def preprocesstext(text):
    # convert text to lower case
    text = text.lower()

    # remove punctuation from text
    text = re.sub(r'[^a-z0-9\s]','',text)

    # Normalize whitespace
    text = re.sub(r'\s+',' ',text)

    # remove urls
    text = re.sub(r'http\S+|www\S+|https\S+','',text)

    # trim
    text.strip()

    return text


# create a dummy dataset
data = {'text':['Hello World.!!','Learning ML is fun','Vector DB is super','World! https://example.com','']}

# Structure the data by Loading it to dataframe
df = pd.DataFrame(data)

# add new new columns
df['id'] = range(len(df))
df['cleaned_data'] = df['text'].apply(preprocesstext)

# drop empty rows
df = df.dropna(subset='cleaned_data')

# filter short texts
df = df[df['cleaned_data'].str.len()>0]

# complete text to token conversion
def tokenize(text):
    return text.split()

all_tokens = []

for text in df['cleaned_data']:
    tokens = tokenize(text)
    for t in tokens:
        all_tokens.append(t)

# build vocab
vocab = {t:i+1 for i, t in enumerate(set(all_tokens))}

# add UNK to vocab to handle unknown work
vocab['<UNK>'] = 0


print(vocab)

print(all_tokens)

