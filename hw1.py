# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Assignment 1

# %%
import spacy
import pandas as pd 
import numpy as np


# %%
sp = spacy.load("en_core_web_lg")

#read the tweets
df = pd.read_csv("Twitter.txt", '\t', names=['querytweettime', 'title'])
docs = df["title"]
print(df.dtypes)


# %%
import tokenizer
import io
import pickle
    
docs_mini = df.head(20)


try:
    with open('tokenizedDataFrame.bin', 'rb+') as pickle_file:
        docs_tokenized = pickle.load(pickle_file)
except:
    docs_tokenized = df.apply(tokenizer.tokenize, 1, spacy=sp)
    with open('tokenizedDataFrame.bin', 'wb') as pickle_file:
        rawdocs = pickle.dump(docs_tokenized, pickle_file)
print(docs_tokenized)


# %%
from index import InvertedIndex, indexDocs
invIndex = InvertedIndex()


for label, data in docs_tokenized.iterrows():
    indexDocs(data, invIndex)

print(invIndex)


# %%
a = invIndex.dict()
print(len(a.keys()))


# %%
import weighting
weights = weighting.indexWeighting(invIndex)
print(weights)



# %%
weights_vectorized = weighting.vectorizeWeighting(weights)
print(weights_vectorized)


# %%



